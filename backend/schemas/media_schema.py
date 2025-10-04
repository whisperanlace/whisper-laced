# backend/schemas/media_schema.py
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class MediaBase(BaseModel):
    file_url: str

class MediaCreate(MediaBase):
    pass

class MediaResponse(MediaBase):
    id: int
    uploaded_at: datetime
    user_id: Optional[int] = None

    class Config:
        from_attributes = True
