from backend.core.password import verify_password


from __future__ import annotations
import os, sys, datetime as dt
from typing import Optional, Any
from fastapi import APIRouter, Depends, HTTPException, Body
from sqlalchemy.orm import Session

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from backend.db import get_db

router = APIRouter(prefix="/auth", tags=["auth-debug"])

def _get_hasher():
    try:
        from passlib.hash import bcrypt as pl_bcrypt
        def verify(plain: str, hashed: str) -> bool:
            try: return pl_bcrypt.verify(plain, hashed)
            except Exception: return False
        return verify
    except Exception:
        pass
    try:
        def verify(plain: str, hashed: str) -> bool:
            try: return bcrypt.checkpw(plain.encode("utf-8"), hashed.encode("utf-8"))
            except Exception: return False
        return verify
    except Exception:
        pass
    return lambda p,h: False

VERIFY = _get_hasher()

def _find_user_by_email(db: Session, email: str) -> Optional[Any]:
    try:
        from backend.models import User
        return db.query(User).filter(User.email == email).first()
    except Exception:
        return None

def _user_password_hash(user: Any) -> Optional[str]:
    for field in ("hashed_password","password_hash","password"):
        if hasattr(user, field):
            v = getattr(user, field)
            if isinstance(v, str) and v:
                return v
    return None

def _create_token(claims: dict) -> str:
    try:
        from backend.core import auth
        if hasattr(auth, "create_access_token"):
            return auth.create_access_token(claims)
    except Exception:
        pass
    secret = os.getenv("SECRET_KEY", "dev-secret-change-me")
    alg = os.getenv("ALGORITHM", "HS256")
    exp_minutes = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "60"))
    payload = claims.copy()
    payload["exp"] = dt.datetime.utcnow() + dt.timedelta(minutes=exp_minutes)
    try:
        from jose import jwt as jose_jwt
        return jose_jwt.encode(payload, secret, algorithm=alg)
    except Exception:
        import jwt as pyjwt
        return pyjwt.encode(payload, secret, algorithm=alg)

@router.post("/token_debug")
def token_debug(payload: dict = Body(...), db: Session = Depends(get_db)):
    # expects {"email": "...", "password": "..."}
    email = payload.get("email")
    password = payload.get("password")
    if not email or not password:
        raise HTTPException(status_code=400, detail="email and password required")

    user = _find_user_by_email(db, email)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    hashed = _user_password_hash(user)
    if not hashed or not VERIFY(password, hashed):
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    claims = {"sub": str(getattr(user, "id", "")), "email": getattr(user, "email", None)}
    token = _create_token(claims)
    return {"access_token": token, "token_type": "bearer"}





