from sqlalchemy.orm import Session
from typing import List
from backend.models import Comment

def create_comment(db: Session, user_id: int, post_id: int, content: str) -> Comment:
    c = Comment(user_id=user_id, post_id=post_id, content=content)
    db.add(c)
    db.commit()
    db.refresh(c)
    return c

def list_comments(db: Session, post_id: int) -> List[Comment]:
    return db.query(Comment).filter(Comment.post_id == post_id).all()

