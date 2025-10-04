from pydantic import BaseModel
from datetime import datetime

class AvatarCreate(BaseModel):
    image_url: str

class AvatarResponse(BaseModel):
    id: int
    image_url: str
    created_at: datetime

    class Config:
        from_attributes = True
