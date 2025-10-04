from sqlalchemy.orm import Session
from backend.models import User
from backend.services.security import hash_password, verify_password

def create_user(db: Session, email: str, password: str) -> User:
    if db.query(User).filter(User.email == email).first():
        raise ValueError("Email already registered")
    u = User(email=email, hashed_password=hash_password(password))
    db.add(u); db.commit(); db.refresh(u)
    return u

def authenticate(db: Session, email: str, password: str) -> User | None:
    u = db.query(User).filter(User.email == email).first()
    if not u: return None
    if not verify_password(password, u.hashed_password): return None
    return u

