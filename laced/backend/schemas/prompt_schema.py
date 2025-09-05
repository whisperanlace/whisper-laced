# schemas/prompt_schema.py

from pydantic import BaseModel
from typing import Optional, Dict
from datetime import datetime


class PromptCreate(BaseModel):
    text: str
    metadata: Optional[Dict] = None
    created_at: Optional[datetime] = None


class PromptUpdate(BaseModel):
    text: Optional[str] = None
    metadata: Optional[Dict] = None


class PromptOut(BaseModel):
    id: int
    user_id: int
    text: str
    metadata: Optional[Dict] = None
    created_at: Optional[datetime]

    class Config:
        orm_mode = True
