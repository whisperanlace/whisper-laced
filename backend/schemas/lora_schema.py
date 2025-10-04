from pydantic import BaseModel
from datetime import datetime

class LoRACreate(BaseModel):
    name: str
    path: str

class LoRAResponse(BaseModel):
    id: int
    name: str
    path: str
    uploaded_at: datetime

    class Config:
        from_attributes = True
