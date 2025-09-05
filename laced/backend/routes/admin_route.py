from fastapi import APIRouter, Depends, HTTPException
from backend.controllers.admin_controller import AdminController
from backend.schemas.admin_schema import AdminActionSchema
from backend.utils.dependencies import get_current_user

router = APIRouter()
admin_ctrl = AdminController()

@router.post("/action")
async def perform_admin_action(payload: AdminActionSchema, current_user=Depends(get_current_user)):
    try:
        return await admin_ctrl.perform_action(payload, current_user)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
