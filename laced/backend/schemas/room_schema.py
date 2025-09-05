# schemas/room_schema.py

from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class RoomCreate(BaseModel):
    name: str
    private: bool = False
    description: Optional[str] = None


class RoomOut(BaseModel):
    id: int
    name: str
    private: bool
    description: Optional[str] = None
    created_at: datetime

    class Config:
        orm_mode = True
