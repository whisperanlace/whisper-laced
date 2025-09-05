# schemas/persona_schema.py

from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class PersonaCreate(BaseModel):
    name: str
    description: Optional[str] = None
    attributes: Optional[dict] = None


class PersonaOut(BaseModel):
    id: int
    user_id: int
    name: str
    description: Optional[str] = None
    attributes: Optional[dict] = None
    created_at: datetime

    class Config:
        orm_mode = True
