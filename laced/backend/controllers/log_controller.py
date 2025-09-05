from fastapi import APIRouter, Depends, HTTPException
from backend.services import LogService
from backend.schemas.log_schema import LogCreateSchema
from backend.utils.dependencies import get_current_user, get_admin_user

router = APIRouter(prefix="/logs", tags=["Logs"])
log_service = LogService()

@router.post("/")
async def create_log(payload: LogCreateSchema, _user=Depends(get_admin_user)):
    return await log_service.create_log(payload)

@router.get("/")
async def get_logs(user=Depends(get_current_user)):
    # Admin sees all, users see their own
    if getattr(user, "is_admin", False):
        return await log_service.get_logs()
    return await log_service.get_logs(user=user)

@router.delete("/{log_id}")
async def delete_log(log_id: str, _admin=Depends(get_admin_user)):
    ok = await log_service.delete_log(log_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Log not found")
    return {"detail": "Log deleted"}
