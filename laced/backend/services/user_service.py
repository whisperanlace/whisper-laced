# services/User_service.py
from sqlalchemy.orm import Session
from app.models.User import User
from app.schemas.User_schemas import UserSchema
from fastapi import HTTPException, status

class UserService:
    async def list_users(self, db: Session):
        return db.query(User).all()

    async def get_user(self, db: Session, user_id: int):
        user = db.query(User).filter(User.id == user_id).first()
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        return user

    async def update_user(self, db: Session, user_id: int, payload: UserSchema):
        user = db.query(User).filter(User.id == user_id).first()
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        for key, value in payload.dict().items():
            setattr(user, key, value)
        db.commit()
        db.refresh(user)
        return user

    async def deactivate_user(self, db: Session, user_id: int):
        user = db.query(User).filter(User.id == user_id).first()
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        user.is_active = False
        db.commit()
        return {"status": "deactivated"}
