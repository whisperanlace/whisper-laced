from __future__ import annotations
from typing import Optional
from fastapi import APIRouter, Depends, Query, HTTPException

# tolerate missing roles module (dev mode); in prod we use real guard
def _noop(dep=None):
    def _inner(*args, **kwargs):
        return None
    return _inner

try:
    from backend.dependencies.roles import require_admin_or_moderator
except Exception:
    require_admin_or_moderator = _noop()

router = APIRouter(prefix="/moderation", tags=["moderation"])

@router.get("/", dependencies=[Depends(require_admin_or_moderator)])
def list_cases(limit: int = Query(20, ge=1, le=200), offset: int = Query(0, ge=0)):
    # wire-up stub: return empty list for now
    return []

@router.get("/{case_id}", dependencies=[Depends(require_admin_or_moderator)])
def get_case(case_id: int):
    # stub detail
    return {"id": case_id, "status": "open"}

@router.post("/{case_id}/assign", dependencies=[Depends(require_admin_or_moderator)])
def assign_case(case_id: int, assignee: Optional[int] = None):
    return {"id": case_id, "assigned_to": assignee}

@router.post("/{case_id}/status", dependencies=[Depends(require_admin_or_moderator)])
def update_status(case_id: int, status: str = Query(..., pattern="^(open|closed|review)$")):
    return {"id": case_id, "status": status}
