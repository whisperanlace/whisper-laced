# services/Lounge_service.py
from sqlalchemy.orm import Session
from app.models.Lounge import Lounge

class LoungeService:
    async def create_lounge(self, db: Session, name: str):
        lounge = Lounge(name=name)
        db.add(lounge)
        db.commit()
        db.refresh(lounge)
        return lounge
