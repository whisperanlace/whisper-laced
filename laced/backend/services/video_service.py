# services/Video_service.py
from sqlalchemy.orm import Session
from app.models.Video import Video
from fastapi import UploadFile, HTTPException, status
import os
from uuid import uuid4

class VideoService:
    async def upload_video(self, db: Session, user_id: int, file: UploadFile):
        if file.content_type not in ["video/mp4", "video/mov"]:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid file type")
        folder = "videos"
        os.makedirs(folder, exist_ok=True)
        filename = f"{uuid4()}_{file.filename}"
        path = os.path.join(folder, filename)
        with open(path, "wb") as f:
            f.write(await file.read())
        video = Video(user_id=user_id, filename=filename, path=path)
        db.add(video)
        db.commit()
        db.refresh(video)
        return video

    async def list_videos(self, db: Session, user_id: int):
        return db.query(Video).filter(Video.user_id == user_id).all()
