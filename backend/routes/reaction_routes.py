from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.schemas.reaction_schema import ReactionCreate, ReactionOut
from backend.services.reaction_service import add_reaction_to_post, add_reaction_to_comment
from backend.models import get_db
from backend.dependencies.auth import get_current_user

router = APIRouter(prefix="/reaction", tags=["reaction"])

@router.post("/", response_model=ReactionOut)
def react(data: ReactionCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    if data.target_type == "post":
        return add_reaction_to_post(db, user_id=user.id, post_id=data.target_id, rtype=data.type)
    elif data.target_type == "comment":
        return add_reaction_to_comment(db, user_id=user.id, comment_id=data.target_id, rtype=data.type)
    raise HTTPException(status_code=400, detail="Invalid target_type")

