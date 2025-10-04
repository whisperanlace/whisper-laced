from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from backend.db import get_db
from backend.schemas.video_schema import VideoCreate, VideoResponse
from backend.services import video_service
from backend.dependencies.auth import get_current_user

router = APIRouter()

@router.post("/", response_model=VideoResponse)
def upload_video(video: VideoCreate, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    return video_service.create_video(db, video, current_user.id)

@router.get("/", response_model=List[VideoResponse])
def list_videos(db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    return video_service.list_videos(db)
