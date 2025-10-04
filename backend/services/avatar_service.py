from sqlalchemy.orm import Session
from backend.models import Avatar
from backend.schemas.avatar_schema import AvatarCreate

def create_avatar(db: Session, avatar: AvatarCreate, user_id: int):
    db_avatar = Avatar(image_url=avatar.image_url, user_id=user_id)
    db.add(db_avatar)
    db.commit()
    db.refresh(db_avatar)
    return db_avatar

def list_avatars(db: Session):
    return db.query(Avatar).all()

