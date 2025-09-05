# services/Analytics_service.py
from sqlalchemy.orm import Session
from app.models.Analytics import Analytics

class AnalyticsService:
    async def log_event(self, db: Session, event: str, user_id: int):
        analytics = Analytics(user_id=user_id, event=event)
        db.add(analytics)
        db.commit()
        db.refresh(analytics)
        return analytics
