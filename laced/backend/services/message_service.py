# services/Message_service.py
from sqlalchemy.orm import Session
from app.models.Message import Message
from fastapi import HTTPException, status

class MessageService:
    async def send_message(self, db: Session, room_id: int, user_id: int, content: str):
        message = Message(room_id=room_id, user_id=user_id, content=content)
        db.add(message)
        db.commit()
        db.refresh(message)
        return message

    async def list_messages(self, db: Session, room_id: int):
        return db.query(Message).filter(Message.room_id == room_id).all()
