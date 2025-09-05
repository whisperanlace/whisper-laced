# services/Image_service.py
from sqlalchemy.orm import Session
from app.models.Image import Image
from fastapi import UploadFile, HTTPException, status
import os
from uuid import uuid4

class ImageService:
    async def upload_image(self, db: Session, user_id: int, file: UploadFile):
        if file.content_type not in ["image/png", "image/jpeg"]:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid file type")
        folder = "images"
        os.makedirs(folder, exist_ok=True)
        filename = f"{uuid4()}_{file.filename}"
        path = os.path.join(folder, filename)
        with open(path, "wb") as f:
            f.write(await file.read())
        image = Image(user_id=user_id, filename=filename, path=path)
        db.add(image)
        db.commit()
        db.refresh(image)
        return image
