# controllers/lora_upload_log_controller.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from services.lora_upload_log_service import LoraUploadLogService
from utils.dependencies import get_db, get_current_user

router = APIRouter(prefix="/lora-uploads", tags=["Lora Upload Logs"])


@router.get("/", summary="List user's LoRA upload logs")
def list_logs(db: Session = Depends(get_db), user=Depends(get_current_user)):
    return LoraUploadLogService.list_logs(db, user.id)
