from fastapi import APIRouter, Depends
from typing import List
from backend.controllers.logs_controller import LogsController
from backend.schemas.logs_schema import LogsSchema
from backend.utils.dependencies import get_current_user

router = APIRouter()
logs_ctrl = LogsController()

@router.get("/", response_model=List[LogsSchema])
async def get_logs(current_user=Depends(get_current_user)):
    return await logs_ctrl.get_logs(current_user)
