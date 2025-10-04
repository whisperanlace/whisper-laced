from pydantic import BaseModel
from typing import Optional

class PostCreate(BaseModel):
    content: str
    community_id: Optional[int] = None
    lounge_id: Optional[int] = None
    image_path: Optional[str] = None

class PostOut(BaseModel):
    id: int
    user_id: int
    community_id: Optional[int] = None
    lounge_id: Optional[int] = None
    content: str
    image_path: Optional[str] = None
    class Config:
        from_attributes = True
