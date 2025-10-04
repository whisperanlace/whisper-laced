from sqlalchemy.orm import Session
from backend.models import Media

def create_media(db: Session, type: str, url: str, user_id: int):
    db_media = Media(type=type, url=url, user_id=user_id)
    db.add(db_media)
    db.commit()
    db.refresh(db_media)
    return db_media

def list_media(db: Session):
    return db.query(Media).all()

