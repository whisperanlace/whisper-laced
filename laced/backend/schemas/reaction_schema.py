# schemas/reaction_schema.py

from pydantic import BaseModel


class ReactionCreate(BaseModel):
    target_type: str
    target_id: int
    type: str  # e.g., "like", "love", "dislike"


class ReactionOut(BaseModel):
    id: int
    user_id: int
    target_type: str
    target_id: int
    type: str

    class Config:
        orm_mode = True
