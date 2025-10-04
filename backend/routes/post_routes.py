from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.schemas.post_schema import PostCreate, PostOut
from backend.services.post_service import create_post, list_posts
from backend.models import get_db
from backend.dependencies.auth import get_current_user

router = APIRouter(prefix="/post", tags=["post"])

@router.post("/", response_model=PostOut)
def create(data: PostCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    return create_post(db, user_id=user.id, content=data.content, community_id=data.community_id, lounge_id=data.lounge_id, image_path=data.image_path)

@router.get("/", response_model=list[PostOut])
def list_all(community_id: int | None = None, lounge_id: int | None = None, limit: int = 50, offset: int = 0, db: Session = Depends(get_db)):
    return list_posts(db, community_id=community_id, lounge_id=lounge_id, limit=limit, offset=offset)

