from pydantic import BaseModel
from typing import Optional, List

class CommunityCreate(BaseModel):
    name: str
    description: Optional[str] = None

class CommunityOut(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    owner_id: int
    class Config:
        from_attributes = True
