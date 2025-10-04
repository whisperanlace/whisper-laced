from sqlalchemy.orm import Session
from typing import List
from backend.models import Post

def create_post(db: Session, user_id: int, content: str, community_id: int | None, lounge_id: int | None, image_path: str | None) -> Post:
    post = Post(user_id=user_id, content=content, community_id=community_id, lounge_id=lounge_id, image_path=image_path)
    db.add(post)
    db.commit()
    db.refresh(post)
    return post

def list_posts(db: Session, community_id: int | None = None, lounge_id: int | None = None, limit: int = 50, offset: int = 0) -> List[Post]:
    q = db.query(Post).order_by(Post.created_at.desc())
    if community_id:
        q = q.filter(Post.community_id == community_id)
    if lounge_id:
        q = q.filter(Post.lounge_id == lounge_id)
    return q.offset(offset).limit(limit).all()

