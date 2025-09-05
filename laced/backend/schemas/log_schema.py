# schemas/log_schema.py

from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class LogOut(BaseModel):
    id: int
    level: str
    message: str
    source: Optional[str] = None
    created_at: datetime

    class Config:
        orm_mode = True
