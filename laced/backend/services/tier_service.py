# services/Tier_service.py
from sqlalchemy.orm import Session
from app.models.Tier import Tier

class TierService:
    async def create_tier(self, db: Session, name: str, benefits: str):
        tier = Tier(name=name, benefits=benefits)
        db.add(tier)
        db.commit()
        db.refresh(tier)
        return tier
