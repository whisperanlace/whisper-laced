# schemas/admin_schema.py

from pydantic import BaseModel
from typing import Optional


class AdminAction(BaseModel):
    user_id: int
    action: str
    reason: Optional[str] = None


class AdminOut(BaseModel):
    id: int
    admin_id: int
    user_id: int
    action: str
    reason: Optional[str] = None
    created_at: str

    class Config:
        orm_mode = True
