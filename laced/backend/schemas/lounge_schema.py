# schemas/lounge_schema.py

from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class LoungeRoomOut(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    private: bool
    created_at: datetime

    class Config:
        orm_mode = True
