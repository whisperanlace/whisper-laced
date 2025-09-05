# schemas/editor_schema.py

from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class EditorAction(BaseModel):
    image_id: int
    action: str
    parameters: Optional[dict] = None


class EditorOut(BaseModel):
    id: int
    user_id: int
    image_id: int
    action: str
    parameters: Optional[dict] = None
    created_at: datetime

    class Config:
        orm_mode = True
