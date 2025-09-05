# services/Persona_service.py
from sqlalchemy.orm import Session
from app.models.Persona import Persona

class PersonaService:
    async def create_persona(self, db: Session, user_id: int, name: str):
        persona = Persona(user_id=user_id, name=name)
        db.add(persona)
        db.commit()
        db.refresh(persona)
        return persona
