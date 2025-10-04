from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from backend.schemas.auth import UserCreate, Login, Token, UserOut
from backend.dependencies.db import get_db
from backend.services.users import create_user, authenticate
from backend.services.security import create_access_token
from backend.services.tokens import create_refresh, revoke_refresh, create_email_verify, use_email_verify, create_password_reset, use_password_reset
from backend.services.email import send_email
from backend.models import User
from backend.services.security import hash_password

router = APIRouter(prefix="/auth", tags=["auth"])

@router.get("/_ping")
def _ping():
    return {"ok": True}

@router.post("/register", response_model=UserOut, status_code=201)
def register(body: UserCreate, db: Session = Depends(get_db)):
    try:
        u = create_user(db, body.email, body.password)
        # issue email verification token (returned inline for now)
        vt = create_email_verify(db, u.id)
        send_email(u.email, "Verify your email", f"Token: {vt.token}")
        return UserOut(id=u.id, email=u.email, created_at=u.created_at, is_verified=u.is_verified)
    except ValueError as e:
        raise HTTPException(status_code=409, detail=str(e))

@router.post("/login", response_model=Token)
def login(body: Login, db: Session = Depends(get_db)):
    u = authenticate(db, body.email, body.password)
    if not u:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    access = create_access_token(u.email, minutes=60)
    r = create_refresh(db, u.id, days=14)
    return Token(access_token=access, refresh_token=r.jti)

@router.post("/refresh", response_model=Token)
def refresh(refresh_token: str = Query(..., alias="rt"), db: Session = Depends(get_db)):
    # very simple: check token exists and not revoked/expired
    from datetime import datetime, timezone
    from backend.models import RefreshToken
    t = db.query(RefreshToken).filter(RefreshToken.jti==refresh_token).first()
    if not t or t.revoked or t.expires_at < datetime.now(timezone.utc):
        raise HTTPException(status_code=401, detail="Invalid refresh token")
    # issue new access (rotate optional; here we keep same refresh)
    user = db.query(User).filter(User.id==t.user_id).first()
    if not user:
        raise HTTPException(status_code=401, detail="User not found")
    access = create_access_token(user.email, minutes=60)
    return Token(access_token=access, refresh_token=refresh_token)

@router.post("/logout")
def logout(refresh_token: str = Query(..., alias="rt"), db: Session = Depends(get_db)):
    revoke_refresh(db, refresh_token)
    return {"ok": True}

@router.post("/verify/request")
def verify_request(email: str = Query(...), db: Session = Depends(get_db)):
    u = db.query(User).filter(User.email==email).first()
    if not u: return {"ok": True}  # do not reveal existence
    vt = create_email_verify(db, u.id)
    send_email(u.email, "Verify your email", f"Token: {vt.token}")
    return {"ok": True}

@router.post("/verify/confirm")
def verify_confirm(token: str = Query(...), db: Session = Depends(get_db)):
    t = use_email_verify(db, token)
    if not t: raise HTTPException(status_code=400, detail="Invalid token")
    u = db.query(User).filter(User.id==t.user_id).first()
    if not u: raise HTTPException(status_code=400, detail="User missing")
    u.is_verified = True; db.commit()
    return {"ok": True}

@router.post("/password/reset/request")
def password_reset_request(email: str = Query(...), db: Session = Depends(get_db)):
    u = db.query(User).filter(User.email==email).first()
    if not u: return {"ok": True}
    pt = create_password_reset(db, u.id)
    send_email(u.email, "Password reset", f"Token: {pt.token}")
    return {"ok": True}

@router.post("/password/reset/confirm")
def password_reset_confirm(token: str = Query(...), new_password: str = Query(...), db: Session = Depends(get_db)):
    t = use_password_reset(db, token)
    if not t: raise HTTPException(status_code=400, detail="Invalid token")
    u = db.query(User).filter(User.id==t.user_id).first()
    if not u: raise HTTPException(status_code=400, detail="User missing")
    u.hashed_password = hash_password(new_password); db.commit()
    return {"ok": True}


