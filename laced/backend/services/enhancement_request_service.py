# services/Enhancement_request_service.py
from sqlalchemy.orm import Session
from app.models.Enhancement_request import EnhancementRequest

class EnhancementRequestService:
    async def create_request(self, db: Session, user_id: int, description: str):
        req = EnhancementRequest(user_id=user_id, description=description)
        db.add(req)
        db.commit()
        db.refresh(req)
        return req
