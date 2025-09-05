from fastapi import APIRouter, Depends
from typing import List
from backend.controllers.activity_controller import ActivityController
from backend.schemas.activity_schema import ActivitySchema
from backend.utils.dependencies import get_current_user

router = APIRouter()
activity_ctrl = ActivityController()

@router.get("/", response_model=List[ActivitySchema])
async def list_activity(current_user=Depends(get_current_user)):
    return await activity_ctrl.list_activity(current_user)
