# schemas/system_flag_schema.py

from pydantic import BaseModel
from datetime import datetime


class SystemFlagCreate(BaseModel):
    target_type: str
    target_id: int
    reason: str


class SystemFlagOut(BaseModel):
    id: int
    user_id: int
    target_type: str
    target_id: int
    reason: str
    created_at: datetime

    class Config:
        orm_mode = True
