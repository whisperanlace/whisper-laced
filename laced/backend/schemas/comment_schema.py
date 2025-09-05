# schemas/comment_schema.py

from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class CommentCreate(BaseModel):
    post_id: int
    content: str
    parent_id: Optional[int] = None


class CommentOut(BaseModel):
    id: int
    user_id: int
    post_id: int
    content: str
    parent_id: Optional[int] = None
    created_at: datetime

    class Config:
        orm_mode = True
