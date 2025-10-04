from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from backend.db import get_db
from backend.schemas.lora_schema import LoRACreate, LoRAResponse
from backend.services import lora_service
from backend.dependencies.auth import get_current_user

router = APIRouter()

@router.post("/", response_model=LoRAResponse)
def upload_lora(lora: LoRACreate, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    return lora_service.create_lora(db, lora, current_user.id)

@router.get("/", response_model=List[LoRAResponse])
def list_loras(db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    return lora_service.list_loras(db)
