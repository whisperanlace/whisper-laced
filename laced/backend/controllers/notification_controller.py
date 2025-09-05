# controllers/notification_controller.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.notification_schema import NotificationOut
from services.notification_service import NotificationService
from utils.dependencies import get_db, get_current_user

router = APIRouter(prefix="/notifications", tags=["Notifications"])


@router.get("/", response_model=list[NotificationOut])
def list_notifications(
    db: Session = Depends(get_db), user=Depends(get_current_user)
):
    return NotificationService.list_user_notifications(db, user.id)


@router.post("/{notification_id}/mark-read")
def mark_notification_read(
    notification_id: int,
    db: Session = Depends(get_db),
    user=Depends(get_current_user),
):
    success = NotificationService.mark_as_read(db, notification_id, user.id)
    if not success:
        raise HTTPException(status_code=404, detail="Notification not found")
    return {"detail": "Notification marked as read"}
