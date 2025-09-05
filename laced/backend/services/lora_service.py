# services/Lora_service.py
from sqlalchemy.orm import Session
from app.models.Lora import LoRA
from app.schemas.Lora_schemas import LoRASchema
from fastapi import UploadFile, HTTPException, status
import os
from uuid import uuid4

class LoRAService:
    async def list_loras(self, db: Session):
        return db.query(LoRA).all()

    async def create_lora(self, db: Session, payload: LoRASchema):
        lora = LoRA(**payload.dict())
        db.add(lora)
        db.commit()
        db.refresh(lora)
        return lora

    async def save_upload(self, db: Session, file: UploadFile):
        if file.content_type not in ["application/octet-stream", "application/zip"]:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid file type")
        folder = "lora_uploads"
        os.makedirs(folder, exist_ok=True)
        filename = f"{uuid4()}_{file.filename}"
        filepath = os.path.join(folder, filename)
        with open(filepath, "wb") as f:
            f.write(await file.read())
        lora = LoRA(filename=filename, path=filepath)
        db.add(lora)
        db.commit()
        db.refresh(lora)
        return lora

    async def get_lora(self, db: Session, lora_id: int):
        lora = db.query(LoRA).filter(LoRA.id == lora_id).first()
        if not lora:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        return lora
