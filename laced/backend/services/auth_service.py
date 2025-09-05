# services/Auth_service.py
from sqlalchemy.orm import Session
from app.models.User import User
from app.schemas.Auth_schemas import LoginSchema
from app.app.security import verify_password, create_access_token, hash_password
from fastapi import HTTPException, status

class AuthService:
    async def authenticate_user(self, db: Session, email: str, password: str) -> User:
        user = db.query(User).filter(User.email == email).first()
        if not user or not verify_password(password, user.hashed_password):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
        return user

    async def register_user(self, db: Session, email: str, username: str, password: str) -> dict:
        existing = db.query(User).filter(User.email == email).first()
        if existing:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")
        hashed = hash_password(password)
        new_user = User(email=email, username=username, hashed_password=hashed)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        token = create_access_token({"sub": new_user.email})
        return {"user_id": new_user.id, "email": new_user.email, "token": token}
