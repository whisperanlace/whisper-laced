from fastapi import APIRouter, Depends
from typing import List
from backend.controllers.notifications_controller import NotificationsController
from backend.schemas.notification_schema import NotificationSchema
from backend.utils.dependencies import get_current_user

router = APIRouter()
notif_ctrl = NotificationsController()

@router.get("/", response_model=List[NotificationSchema])
async def list_notifications(current_user=Depends(get_current_user)):
    return await notif_ctrl.list_notifications(current_user)

@router.put("/{notification_id}/read", response_model=NotificationSchema)
async def mark_read(notification_id: str, current_user=Depends(get_current_user)):
    return await notif_ctrl.mark_read(notification_id, current_user)
