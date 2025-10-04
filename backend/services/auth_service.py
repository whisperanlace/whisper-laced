from __future__ import annotations
from sqlalchemy.orm import Session
from sqlalchemy import select, or_
from backend.models import User
from backend.core.password import verify_password

def get_user_by_email_or_username(db: Session, login: str) -> User | None:
    stmt = select(User).where(or_(User.email == login, User.username == login))
    return db.execute(stmt).scalar_one_or_none()

def authenticate_user(db: Session, login: str, password: str) -> User | None:
    user = get_user_by_email_or_username(db, login)
    if not user or not user.hashed_password:
        return None
    if not verify_password(password, user.hashed_password):
        return None
    return user

