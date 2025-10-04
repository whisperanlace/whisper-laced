from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel

from backend.models import TargetType
from backend.models import ReportStatus, ReportReason


class ReportCreate(BaseModel):
    target_type: TargetType
    target_id: int
    reason: ReportReason
    details: Optional[str] = None


class ReportResponse(BaseModel):
    id: int
    reporter_id: Optional[int]
    target_type: TargetType
    target_id: int
    reason: ReportReason
    details: Optional[str]
    status: ReportStatus
    moderation_case_id: Optional[int]
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

