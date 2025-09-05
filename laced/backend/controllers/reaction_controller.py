# controllers/reaction_controller.py

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from schemas.reaction_schema import ReactionCreate, ReactionOut
from services.reaction_service import ReactionService
from utils.dependencies import get_db, get_current_user

router = APIRouter(prefix="/reactions", tags=["Reactions"])


@router.post("/", response_model=ReactionOut)
def add_reaction(
    reaction: ReactionCreate,
    db: Session = Depends(get_db),
    user=Depends(get_current_user),
):
    return ReactionService.add_reaction(db, user.id, reaction)


@router.delete("/{reaction_id}", status_code=status.HTTP_204_NO_CONTENT)
def remove_reaction(
    reaction_id: int,
    db: Session = Depends(get_db),
    user=Depends(get_current_user),
):
    success = ReactionService.remove_reaction(db, reaction_id, user.id)
    if not success:
        raise HTTPException(status_code=404, detail="Reaction not found")
