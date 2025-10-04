from pydantic import BaseModel
from typing import Optional

class MotionCreate(BaseModel):
    title: str
    description: Optional[str] = None
    community_id: Optional[int] = None
    lounge_id: Optional[int] = None

class MotionOut(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    community_id: Optional[int] = None
    lounge_id: Optional[int] = None
    status: str
    created_by: int
    class Config:
        from_attributes = True
