# services/Reaction_service.py
from sqlalchemy.orm import Session
from app.models.Reaction import Reaction
from fastapi import HTTPException, status

class ReactionService:
    async def add_reaction(self, db: Session, user_id: int, payload: dict):
        reaction = Reaction(user_id=user_id, **payload)
        db.add(reaction)
        db.commit()
        db.refresh(reaction)
        return reaction

    async def remove_reaction(self, db: Session, user_id: int, payload: dict):
        reaction = db.query(Reaction).filter(
            Reaction.user_id == user_id,
            Reaction.target_id == payload["target_id"],
            Reaction.type == payload["type"]
        ).first()
        if reaction:
            db.delete(reaction)
            db.commit()
        return reaction
