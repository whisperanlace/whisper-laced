# schemas/notification_schema.py

from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class NotificationCreate(BaseModel):
    message: str
    type: str
    read: bool = False


class NotificationOut(BaseModel):
    id: int
    user_id: int
    message: str
    type: str
    read: bool
    created_at: datetime

    class Config:
        orm_mode = True
