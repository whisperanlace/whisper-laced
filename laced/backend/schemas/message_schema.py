# schemas/message_schema.py

from pydantic import BaseModel
from datetime import datetime


class MessageCreate(BaseModel):
    room_id: int
    content: str


class MessageOut(BaseModel):
    id: int
    user_id: int
    room_id: int
    content: str
    created_at: datetime

    class Config:
        orm_mode = True
