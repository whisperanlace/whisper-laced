from pydantic import BaseModel, EmailStr
from typing import Optional

class InviteCreate(BaseModel):
    invitee_email: EmailStr
    community_id: Optional[int] = None
    lounge_id: Optional[int] = None

class InviteAccept(BaseModel):
    token: str

class InviteOut(BaseModel):
    id: int
    inviter_id: int
    invitee_email: EmailStr
    token: str
    community_id: Optional[int] = None
    lounge_id: Optional[int] = None
    status: str
    class Config:
        from_attributes = True
