# schemas/invite_schema.py

from pydantic import BaseModel
from datetime import datetime


class InviteCreate(BaseModel):
    email: str
    expires_at: datetime


class InviteOut(BaseModel):
    id: int
    inviter_id: int
    email: str
    token: str
    expires_at: datetime
    accepted: bool

    class Config:
        orm_mode = True
