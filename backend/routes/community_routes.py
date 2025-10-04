from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.schemas.community_schema import CommunityCreate, CommunityOut
from backend.services.community_service import create_community, list_communities, add_member
from backend.models import get_db
from backend.dependencies.auth import get_current_user

router = APIRouter(prefix="/community", tags=["community"])

@router.post("/", response_model=CommunityOut)
def create(data: CommunityCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    return create_community(db, owner_id=user.id, name=data.name, description=data.description)

@router.get("/", response_model=list[CommunityOut])
def list_all(db: Session = Depends(get_db)):
    return list_communities(db)

