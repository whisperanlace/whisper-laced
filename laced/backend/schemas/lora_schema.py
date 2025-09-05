# schemas/lora_schema.py

from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class LoraCreate(BaseModel):
    name: str
    description: Optional[str] = None
    version: Optional[str] = None


class LoraOut(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    version: Optional[str] = None
    created_at: datetime

    class Config:
        orm_mode = True
