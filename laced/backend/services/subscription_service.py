# services/Subscription_service.py
from sqlalchemy.orm import Session
from app.models.Subscription import Subscription
from fastapi import HTTPException, status

class SubscriptionService:
    async def create_subscription(self, db: Session, user_id: int, tier: str):
        sub = Subscription(user_id=user_id, tier=tier)
        db.add(sub)
        db.commit()
        db.refresh(sub)
        return sub

    async def get_subscription(self, db: Session, user_id: int):
        return db.query(Subscription).filter(Subscription.user_id == user_id).first()
