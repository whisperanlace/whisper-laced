# schemas/video_schema.py

from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class VideoCreate(BaseModel):
    title: str
    url: str
    description: Optional[str] = None


class VideoOut(BaseModel):
    id: int
    user_id: int
    title: str
    url: str
    description: Optional[str] = None
    created_at: datetime

    class Config:
        orm_mode = True
