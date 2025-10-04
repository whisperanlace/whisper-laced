import time, os
import jwt
from datetime import datetime, timedelta
from typing import Tuple, Dict
from sqlalchemy.orm import Session
from backend.config.settings import settings
from backend.services.hashing import hash_password, verify_password
from backend.models import User
from backend.models import RefreshToken

def create_access_token(sub: str) -> str:
    now = int(time.time())
    exp = now + settings.ACCESS_TOKEN_EXPIRE_MINUTES * 60
    payload = {"sub": sub, "iat": now, "exp": exp}
    return jwt.encode(payload, settings.SECRET_KEY, algorithm=settings.ALGORITHM)

def decode_access_token(token: str) -> Dict:
    try:
        return jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
    except Exception:
        raise ValueError("Invalid or expired token")

def _now_utc() -> datetime: return datetime.utcnow()

def create_refresh_token(db: Session, user_id: int) -> str:
    # Use a random jwt as opaque token; store only its hash in DB
    raw = jwt.encode({"uid": user_id, "ts": int(time.time())}, os.urandom(32), algorithm="HS256")
    token_hash = hash_password(raw)
    expires = _now_utc() + timedelta(days=settings.REFRESH_TOKEN_EXPIRE_DAYS)
    db_rt = RefreshToken(user_id=user_id, token_hash=token_hash, expires_at=expires, revoked=False)
    db.add(db_rt); db.commit(); db.refresh(db_rt)
    return raw

def rotate_refresh_token(db: Session, user_id: int, raw_token: str) -> Tuple[str, str]:
    # revoke old, create new
    from sqlalchemy import select
    # Find a matching token by verifying hash
    rts = db.execute(select(RefreshToken).where(RefreshToken.user_id==user_id, RefreshToken.revoked==False)).scalars().all()
    matched = None
    for rt in rts:
        if verify_password(raw_token, rt.token_hash):
            matched = rt; break
    if not matched or matched.expires_at < _now_utc():
        raise ValueError("Invalid refresh token")
    matched.revoked = True
    db.commit()
    # issue new
    new_raw = create_refresh_token(db, user_id)
    new_access = create_access_token(sub=_email_for_user(db, user_id))
    return new_access, new_raw

def _email_for_user(db: Session, user_id: int) -> str:
    u = db.query(User).filter(User.id==user_id).first()
    return u.email if u else ""


