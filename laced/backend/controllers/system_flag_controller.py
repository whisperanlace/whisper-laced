# controllers/system_flag_controller.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from services.system_flag_service import SystemFlagService
from utils.dependencies import get_db, get_current_user

router = APIRouter(prefix="/flags", tags=["System Flags"])


@router.post("/{item_id}")
def flag_item(
    item_id: int,
    reason: str,
    db: Session = Depends(get_db),
    user=Depends(get_current_user),
):
    flagged = SystemFlagService.flag_item(db, user.id, item_id, reason)
    if not flagged:
        raise HTTPException(status_code=400, detail="Unable to flag item")
    return {"detail": "Item flagged"}
