from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class MetricsCreate(BaseModel):
    event_type: str
    value: Optional[str] = None

class MetricsResponse(BaseModel):
    id: int
    event_type: str
    value: Optional[str]
    timestamp: datetime

    class Config:
        from_attributes = True
