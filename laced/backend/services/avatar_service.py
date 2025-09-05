# services/Avatar_service.py
from sqlalchemy.orm import Session
from app.models.Avatar import Avatar
from fastapi import UploadFile, HTTPException, status
import os
from uuid import uuid4

class AvatarService:
    async def create_avatar(self, db: Session, user_id: int, file: UploadFile):
        if file.content_type not in ["image/png", "image/jpeg"]:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid file type")
        folder = "avatars"
        os.makedirs(folder, exist_ok=True)
        filename = f"{uuid4()}_{file.filename}"
        path = os.path.join(folder, filename)
        with open(path, "wb") as f:
            f.write(await file.read())
        avatar = Avatar(user_id=user_id, filename=filename, path=path)
        db.add(avatar)
        db.commit()
        db.refresh(avatar)
        return avatar

    async def list_avatars(self, db: Session, user_id: int):
        return db.query(Avatar).filter(Avatar.user_id == user_id).all()
