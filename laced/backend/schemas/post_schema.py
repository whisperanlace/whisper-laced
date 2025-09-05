# schemas/post_schema.py

from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class PostCreate(BaseModel):
    title: str
    content: str
    community_id: Optional[int] = None


class PostOut(BaseModel):
    id: int
    user_id: int
    title: str
    content: str
    community_id: Optional[int] = None
    created_at: datetime

    class Config:
        orm_mode = True
