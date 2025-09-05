# schemas/enhancement_request_schema.py

from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class EnhancementRequestCreate(BaseModel):
    title: str
    description: str
    priority: Optional[str] = "medium"


class EnhancementRequestOut(BaseModel):
    id: int
    user_id: int
    title: str
    description: str
    priority: str
    status: str
    created_at: datetime

    class Config:
        orm_mode = True
