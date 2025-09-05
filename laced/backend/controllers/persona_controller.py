# controllers/persona_controller.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.persona_schema import PersonaCreate, PersonaOut
from services.persona_service import PersonaService
from utils.dependencies import get_db, get_current_user

router = APIRouter(prefix="/personas", tags=["Personas"])


@router.post("/", response_model=PersonaOut)
def create_persona(
    persona: PersonaCreate, db: Session = Depends(get_db), user=Depends(get_current_user)
):
    return PersonaService.create_persona(db, user.id, persona)


@router.get("/", response_model=list[PersonaOut])
def list_personas(db: Session = Depends(get_db), user=Depends(get_current_user)):
    return PersonaService.list_personas(db, user.id)
