# services/Lora_upload_log_service.py
from sqlalchemy.orm import Session
from app.models.Lora_upload_log import LoraUploadLog

class LoraUploadLogService:
    async def log_upload(self, db: Session, lora_id: int, status: str):
        log = LoraUploadLog(lora_id=lora_id, status=status)
        db.add(log)
        db.commit()
        db.refresh(log)
        return log
