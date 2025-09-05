# schemas/collection_schema.py

from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class CollectionCreate(BaseModel):
    name: str
    description: Optional[str] = None


class CollectionOut(BaseModel):
    id: int
    user_id: int
    name: str
    description: Optional[str] = None
    created_at: datetime

    class Config:
        orm_mode = True
