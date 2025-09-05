# controllers/admin_controller.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from services.admin_service import AdminService
from utils.dependencies import get_db, get_current_user

router = APIRouter(prefix="/admin", tags=["Admin"])


@router.get("/stats")
def get_system_stats(db: Session = Depends(get_db), user=Depends(get_current_user)):
    if not user.is_admin:
        raise HTTPException(status_code=403, detail="Unauthorized")
    return AdminService.get_system_stats(db)


@router.post("/ban-user/{user_id}")
def ban_user(
    user_id: int,
    db: Session = Depends(get_db),
    user=Depends(get_current_user),
):
    if not user.is_admin:
        raise HTTPException(status_code=403, detail="Unauthorized")
    success = AdminService.ban_user(db, user_id)
    if not success:
        raise HTTPException(status_code=404, detail="User not found")
    return {"detail": "User banned"}
