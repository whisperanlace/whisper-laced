# services/search_service.py
from sqlalchemy.orm import Session
from app.models.Post import Post
from app.models.Comment import Comment

class SearchService:
    async def search(self, db: Session, query: str):
        posts = db.query(Post).filter(Post.content.ilike(f"%{query}%")).all()
        comments = db.query(Comment).filter(Comment.content.ilike(f"%{query}%")).all()
        return {"posts": posts, "comments": comments}
