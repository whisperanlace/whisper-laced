# schemas/avatar_schema.py

from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class AvatarCreate(BaseModel):
    image_url: str
    style: Optional[str] = None


class AvatarOut(BaseModel):
    id: int
    user_id: int
    image_url: str
    style: Optional[str]
    created_at: datetime

    class Config:
        orm_mode = True
