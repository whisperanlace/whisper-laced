from sqlalchemy.orm import Session, joinedload
from passlib.context import CryptContext
from backend.models import User
from backend.db import SessionLocal
from backend.schemas.user_schema import UserCreate
import secrets

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain: str, hashed: str) -> bool:
    return pwd_context.verify(plain, hashed)

def create_user(db: Session, user: UserCreate) -> User:
    db_user = User(
        email=user.email,
        username=user.username,
        hashed_password=get_password_hash(user.password),
        role="user",
        api_key=secrets.token_hex(16),
        api_key_active=True,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def authenticate_user(db: Session, email: str, password: str) -> User | None:
    user = db.query(User).filter(User.email == email).first()
    if not user or not verify_password(password, user.hashed_password):
        return None
    return user

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def get_user_by_id(db: Session, user_id: int):
    return db.query(User).options(joinedload(User.tier)).filter(User.id == user_id).first()

def get_or_create_api_key(user: User) -> str:
    if not user.api_key:
        db = SessionLocal()
        user_in_db = db.query(User).filter(User.id == user.id).first()
        user_in_db.api_key = secrets.token_urlsafe(32)
        db.commit()
        db.refresh(user_in_db)
        db.close()
        return user_in_db.api_key
    return user.api_key

