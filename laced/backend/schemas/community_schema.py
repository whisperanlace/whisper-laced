# schemas/community_schema.py

from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class CommunityCreate(BaseModel):
    name: str
    description: Optional[str] = None
    private: bool = False


class CommunityOut(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    private: bool
    created_at: datetime

    class Config:
        orm_mode = True
