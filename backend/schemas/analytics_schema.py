from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class AnalyticsCreate(BaseModel):
    action: str
    details: Optional[str] = None

class AnalyticsResponse(BaseModel):
    id: int
    action: str
    details: Optional[str]
    timestamp: datetime

    class Config:
        from_attributes = True
