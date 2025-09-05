# schemas/image_schema.py

from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class ImageCreate(BaseModel):
    prompt: str
    style: Optional[str] = None
    width: int
    height: int


class ImageOut(BaseModel):
    id: int
    user_id: int
    url: str
    prompt: str
    width: int
    height: int
    created_at: datetime

    class Config:
        orm_mode = True
