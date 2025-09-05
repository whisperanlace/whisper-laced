# services/Room_service.py
from sqlalchemy.orm import Session
from app.models.Room import Room
from fastapi import HTTPException, status

class RoomService:
    async def create_room(self, db: Session, name: str, type: str):
        room = Room(name=name, type=type)
        db.add(room)
        db.commit()
        db.refresh(room)
        return room

    async def list_rooms(self, db: Session):
        return db.query(Room).all()
