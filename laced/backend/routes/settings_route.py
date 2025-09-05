from fastapi import APIRouter, Depends, HTTPException
from backend.controllers.settings_controller import SettingsController
from backend.schemas.settings_schema import SettingsSchema
from backend.utils.dependencies import get_current_user

router = APIRouter()
settings_ctrl = SettingsController()

@router.get("/", response_model=SettingsSchema)
async def get_settings(current_user=Depends(get_current_user)):
    return await settings_ctrl.get_settings(current_user)

@router.put("/", response_model=SettingsSchema)
async def update_settings(payload: SettingsSchema, current_user=Depends(get_current_user)):
    return await settings_ctrl.update_settings(payload, current_user)
