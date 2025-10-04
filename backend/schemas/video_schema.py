from pydantic import BaseModel
from datetime import datetime

class VideoCreate(BaseModel):
    file_url: str

class VideoResponse(BaseModel):
    id: int
    file_url: str
    status: str
    created_at: datetime

    class Config:
        from_attributes = True
