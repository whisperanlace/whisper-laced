from sqlalchemy.orm import Session
from backend.models import LoRA
from backend.schemas.lora_schema import LoRACreate

def create_lora(db: Session, lora_data: LoRACreate, user_id: int) -> LoRA:
    lora = LoRA(**lora_data.dict(), user_id=user_id)
    db.add(lora)
    db.commit()
    db.refresh(lora)
    return lora

def list_loras(db: Session, user_id: int):
    return db.query(LoRA).filter(LoRA.user_id == user_id).all()

