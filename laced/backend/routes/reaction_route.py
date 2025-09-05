# routes/Reaction_route.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.Reaction_schemas import ReactionSchema
from app.services.Reaction_service import ReactionService

router = APIRouter()
service = ReactionService()

@router.post("/", status_code=201)
async def react(payload: ReactionSchema, db: Session = Depends(get_db), current_user=Depends(service.get_current_user)):
    await service.add_reaction(db, current_user, payload)
    return {"status": "ok"}

@router.delete("/", status_code=204)
async def remove_reaction(payload: ReactionSchema, db: Session = Depends(get_db), current_user=Depends(service.get_current_user)):
    await service.remove_reaction(db, current_user, payload)
    return None
