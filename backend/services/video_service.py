from sqlalchemy.orm import Session
from backend.models import Video
from backend.schemas.video_schema import VideoCreate

def create_video(db: Session, video: VideoCreate, user_id: int):
    db_video = Video(file_url=video.file_url, user_id=user_id)
    db.add(db_video)
    db.commit()
    db.refresh(db_video)
    return db_video

def list_videos(db: Session):
    return db.query(Video).all()

