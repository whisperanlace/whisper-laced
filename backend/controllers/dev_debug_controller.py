from __future__ import annotations
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from typing import Optional

from backend.db import get_db
from backend.services import moderation_service, report_service
from backend.models import ModerationStatus, TargetType
from backend.models import ReportStatus

router = APIRouter(prefix="/__dev_phase9", tags=["__dev_phase9"])

@router.get("/moderation")
def dev_list_moderation(
    db: Session = Depends(get_db),
    status: Optional[ModerationStatus] = Query(None),
    target_type: Optional[TargetType] = Query(None),
    assignee_id: Optional[int] = Query(None),
    limit: int = Query(10, ge=1, le=100),
    offset: int = Query(0, ge=0),
):
    items, total = moderation_service.list_cases(db, status=status, target_type=target_type, assignee_id=assignee_id, limit=limit, offset=offset)
    return {"total": total, "items": [ {"id": c.id, "status": c.status, "target_type": c.target_type, "target_id": c.target_id, "is_nsfw": c.is_nsfw } for c in items ]}

@router.get("/reports")
def dev_list_reports(
    db: Session = Depends(get_db),
    status: Optional[ReportStatus] = Query(None),
    target_type: Optional[TargetType] = Query(None),
    limit: int = Query(10, ge=1, le=100),
    offset: int = Query(0, ge=0),
):
    items, total = report_service.list_reports(db, status=status, target_type=target_type, limit=limit, offset=offset)
    return {"total": total, "items": [ {"id": r.id, "status": r.status, "reason": r.reason, "target_type": r.target_type, "target_id": r.target_id } for r in items ]}

