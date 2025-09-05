# services/Feedback_service.py
from sqlalchemy.orm import Session
from app.models.Feedback import Feedback
from fastapi import HTTPException, status

class FeedbackService:
    async def create_feedback(self, db: Session, user_id: int, content: str):
        feedback = Feedback(user_id=user_id, content=content)
        db.add(feedback)
        db.commit()
        db.refresh(feedback)
        return feedback

    async def list_feedback(self, db: Session):
        return db.query(Feedback).all()
