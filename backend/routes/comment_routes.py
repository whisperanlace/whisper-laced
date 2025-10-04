from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.schemas.comment_schema import CommentCreate, CommentOut
from backend.services.comment_service import create_comment, list_comments
from backend.models import get_db
from backend.dependencies.auth import get_current_user

router = APIRouter(prefix="/comment", tags=["comment"])

@router.post("/", response_model=CommentOut)
def create(data: CommentCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    return create_comment(db, user_id=user.id, post_id=data.post_id, content=data.content)

@router.get("/", response_model=list[CommentOut])
def list_for_post(post_id: int, db: Session = Depends(get_db)):
    return list_comments(db, post_id=post_id)

