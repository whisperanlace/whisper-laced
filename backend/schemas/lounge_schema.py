from pydantic import BaseModel
from typing import Optional

class LoungeCreate(BaseModel):
    community_id: int
    name: str
    description: Optional[str] = None

class LoungeOut(BaseModel):
    id: int
    community_id: int
    name: str
    description: Optional[str] = None
    class Config:
        from_attributes = True
