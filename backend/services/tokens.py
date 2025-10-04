from datetime import datetime, timezone, timedelta
from sqlalchemy.orm import Session
from backend.models import RefreshToken, EmailVerifyToken, PasswordResetToken
from backend.services.security import new_random_token, expires_in_minutes

def create_refresh(db: Session, user_id: int, days: int = 14) -> RefreshToken:
    t = RefreshToken(jti=new_random_token(), user_id=user_id,
                     expires_at=datetime.now(timezone.utc)+timedelta(days=days))
    db.add(t); db.commit(); db.refresh(t); return t

def revoke_refresh(db: Session, jti: str):
    t = db.query(RefreshToken).filter(RefreshToken.jti==jti).first()
    if t:
        t.revoked = True; db.commit()

def create_email_verify(db: Session, user_id: int, hours: int = 24) -> EmailVerifyToken:
    t = EmailVerifyToken(token=new_random_token(), user_id=user_id,
                         expires_at=datetime.now(timezone.utc)+timedelta(hours=hours))
    db.add(t); db.commit(); db.refresh(t); return t

def use_email_verify(db: Session, token: str) -> EmailVerifyToken | None:
    t = db.query(EmailVerifyToken).filter(EmailVerifyToken.token==token, EmailVerifyToken.used==False).first()
    if not t: return None
    t.used = True; db.commit(); db.refresh(t); return t

def create_password_reset(db: Session, user_id: int, hours: int = 2) -> PasswordResetToken:
    t = PasswordResetToken(token=new_random_token(), user_id=user_id,
                           expires_at=datetime.now(timezone.utc)+timedelta(hours=hours))
    db.add(t); db.commit(); db.refresh(t); return t

def use_password_reset(db: Session, token: str) -> PasswordResetToken | None:
    t = db.query(PasswordResetToken).filter(PasswordResetToken.token==token, PasswordResetToken.used==False).first()
    if not t: return None
    t.used = True; db.commit(); db.refresh(t); return t

