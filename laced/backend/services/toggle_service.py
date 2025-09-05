# services/Toggle_service.py
from sqlalchemy.orm import Session
from app.models.Toggle import Toggle

class ToggleService:
    async def set_toggle(self, db: Session, name: str, value: bool):
        toggle = Toggle(name=name, value=value)
        db.add(toggle)
        db.commit()
        db.refresh(toggle)
        return toggle
