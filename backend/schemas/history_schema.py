from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class HistoryCreate(BaseModel):
    user_id: int
    action: str

class HistoryResponse(BaseModel):
    id: int
    user_id: int
    action: str
    timestamp: datetime

    class Config:
        from_attributes = True
