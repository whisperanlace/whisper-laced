from __future__ import annotations

from typing import Optional, List, Tuple, Dict
from sqlalchemy.orm import Session

from backend.models import ModerationCase, ModerationStatus, TargetType
from backend.models import ReportStatus


def create_case(
    db: Session,
    *,
    target_type: TargetType,
    target_id: int,
    reason: Optional[str] = None,
    detected_labels: Optional[Dict[str, float]] = None,
    is_nsfw: bool = False,
    created_by_id: Optional[int] = None,
    assigned_to_id: Optional[int] = None,
) -> ModerationCase:
    case = ModerationCase(
        target_type=target_type,
        target_id=target_id,
        reason=reason,
        detected_labels=detected_labels,
        is_nsfw=is_nsfw,
        created_by_id=created_by_id,
        assigned_to_id=assigned_to_id,
        status=ModerationStatus.pending,
    )
    db.add(case)
    db.commit()
    db.refresh(case)
    return case


def list_cases(
    db: Session,
    *,
    status: Optional[ModerationStatus] = None,
    target_type: Optional[TargetType] = None,
    assignee_id: Optional[int] = None,
    limit: int = 50,
    offset: int = 0,
) -> Tuple[List[ModerationCase], int]:
    q = db.query(ModerationCase)
    if status:
        q = q.filter(ModerationCase.status == status)
    if target_type:
        q = q.filter(ModerationCase.target_type == target_type)
    if assignee_id:
        q = q.filter(ModerationCase.assigned_to_id == assignee_id)
    total = q.count()
    items = (
        q.order_by(ModerationCase.created_at.desc())
        .offset(offset)
        .limit(limit)
        .all()
    )
    return items, total


def get_case(db: Session, case_id: int) -> Optional[ModerationCase]:
    return db.query(ModerationCase).filter(ModerationCase.id == case_id).first()


def assign_case(db: Session, case_id: int, user_id: int) -> ModerationCase:
    case = get_case(db, case_id)
    if not case:
        raise ValueError("Moderation case not found")
    case.assigned_to_id = user_id
    db.commit()
    db.refresh(case)
    return case


def update_status(
    db: Session,
    case_id: int,
    status: ModerationStatus,
    resolution_notes: Optional[str] = None,
    is_nsfw: Optional[bool] = None,
) -> ModerationCase:
    case = get_case(db, case_id)
    if not case:
        raise ValueError("Moderation case not found")

    case.status = status
    if resolution_notes is not None:
        case.resolution_notes = resolution_notes
    if is_nsfw is not None:
        case.is_nsfw = is_nsfw

    if status in (ModerationStatus.approved, ModerationStatus.rejected):
        for r in case.reports:
            if r.status != ReportStatus.closed:
                r.status = ReportStatus.closed

    db.commit()
    db.refresh(case)
    return case

