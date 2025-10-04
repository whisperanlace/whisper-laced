from __future__ import annotations
from typing import Optional, Dict, Any, List
from datetime import datetime
from pydantic import BaseModel

from backend.models import TargetType, ModerationStatus


class ModerationCreate(BaseModel):
    target_type: TargetType
    target_id: int
    reason: Optional[str] = None
    detected_labels: Optional[Dict[str, float]] = None
    is_nsfw: bool = False
    created_by_id: Optional[int] = None
    assigned_to_id: Optional[int] = None


class ModerationAssign(BaseModel):
    assigned_to_id: int


class ModerationUpdateStatus(BaseModel):
    status: ModerationStatus
    resolution_notes: Optional[str] = None
    is_nsfw: Optional[bool] = None


class ModerationResponse(BaseModel):
    id: int
    target_type: TargetType
    target_id: int
    status: ModerationStatus
    reason: Optional[str]
    detected_labels: Optional[Dict[str, float]]
    is_nsfw: bool
    created_by_id: Optional[int]
    assigned_to_id: Optional[int]
    resolution_notes: Optional[str]
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class ModerationListResponse(BaseModel):
    items: List[ModerationResponse]
    total: int

