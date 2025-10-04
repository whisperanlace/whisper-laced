from pydantic import BaseModel
from typing import Literal, Optional

class ReactionCreate(BaseModel):
    target_type: Literal["post", "comment"]
    target_id: int
    type: str = "like"

class ReactionOut(BaseModel):
    id: int
    user_id: int
    post_id: Optional[int] = None
    comment_id: Optional[int] = None
    type: str
    class Config:
        from_attributes = True
