from pydantic import BaseModel
from datetime import datetime

class UploadCreate(BaseModel):
    filename: str
    file_url: str

class UploadResponse(BaseModel):
    id: int
    filename: str
    file_url: str
    uploaded_at: datetime

    class Config:
        from_attributes = True
