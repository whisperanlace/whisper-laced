# schemas/feedback_schema.py

from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class FeedbackCreate(BaseModel):
    message: str
    rating: Optional[int] = None


class FeedbackOut(BaseModel):
    id: int
    user_id: int
    message: str
    rating: Optional[int] = None
    created_at: datetime

    class Config:
        orm_mode = True
