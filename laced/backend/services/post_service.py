# services/Post_service.py
from sqlalchemy.orm import Session
from app.models.Post import Post

class PostService:
    async def create_post(self, db: Session, user_id: int, content: str):
        post = Post(user_id=user_id, content=content)
        db.add(post)
        db.commit()
        db.refresh(post)
        return post
