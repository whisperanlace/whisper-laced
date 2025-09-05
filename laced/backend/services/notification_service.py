# services/Notification_service.py
from sqlalchemy.orm import Session
from app.models.Notification import Notification

class NotificationService:
    async def create_notification(self, db: Session, user_id: int, content: str):
        notification = Notification(user_id=user_id, content=content)
        db.add(notification)
        db.commit()
        db.refresh(notification)
        return notification

    async def list_notifications(self, db: Session, user_id: int):
        return db.query(Notification).filter(Notification.user_id == user_id).all()
