# schemas/report_schema.py

from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class ReportCreate(BaseModel):
    target_type: str  # e.g., "post", "comment", "user"
    target_id: int
    reason: str


class ReportOut(BaseModel):
    id: int
    reporter_id: int
    target_type: str
    target_id: int
    reason: str
    created_at: datetime

    class Config:
        orm_mode = True
