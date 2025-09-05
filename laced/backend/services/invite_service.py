# services/Invite_service.py
from sqlalchemy.orm import Session
from app.models.Invite import Invite

class InviteService:
    async def send_invite(self, db: Session, sender_id: int, recipient_email: str):
        invite = Invite(sender_id=sender_id, recipient_email=recipient_email)
        db.add(invite)
        db.commit()
        db.refresh(invite)
        return invite
