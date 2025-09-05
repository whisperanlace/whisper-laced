from fastapi import APIRouter, Depends
from backend.controllers.toggle_controller import ToggleController
from backend.schemas.toggle_schema import ToggleSchema
from backend.utils.dependencies import get_current_user
from typing import List

router = APIRouter()
toggle_ctrl = ToggleController()

@router.get("/", response_model=List[ToggleSchema])
async def list_toggles(current_user=Depends(get_current_user)):
    return await toggle_ctrl.list_toggles(current_user)

@router.put("/{toggle_name}", response_model=ToggleSchema)
async def update_toggle(toggle_name: str, payload: ToggleSchema, current_user=Depends(get_current_user)):
    return await toggle_ctrl.update_toggle(toggle_name, payload, current_user)
