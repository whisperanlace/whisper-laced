# schemas/activity_schema.py

from pydantic import BaseModel
from datetime import datetime


class ActivityOut(BaseModel):
    id: int
    user_id: int
    action: str
    target_type: str
    target_id: int
    created_at: datetime

    class Config:
        orm_mode = True
