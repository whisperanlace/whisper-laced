# controllers/settings_controller.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.settings_schema import SettingsUpdate, SettingsOut
from services.settings_service import SettingsService
from utils.dependencies import get_db, get_current_user

router = APIRouter(prefix="/settings", tags=["Settings"])


@router.get("/", response_model=SettingsOut)
def get_user_settings(
    db: Session = Depends(get_db), user=Depends(get_current_user)
):
    return SettingsService.get_settings(db, user.id)


@router.put("/", response_model=SettingsOut)
def update_user_settings(
    settings: SettingsUpdate,
    db: Session = Depends(get_db),
    user=Depends(get_current_user),
):
    updated = SettingsService.update_settings(db, user.id, settings)
    if not updated:
        raise HTTPException(status_code=404, detail="Settings not found")
    return updated
