# services/Comment_service.py
from sqlalchemy.orm import Session
from app.models.Comment import Comment

class CommentService:
    async def add_comment(self, db: Session, user_id: int, post_id: int, content: str):
        comment = Comment(user_id=user_id, post_id=post_id, content=content)
        db.add(comment)
        db.commit()
        db.refresh(comment)
        return comment
