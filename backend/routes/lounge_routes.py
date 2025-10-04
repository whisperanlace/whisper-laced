from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.schemas.lounge_schema import LoungeCreate, LoungeOut
from backend.services.lounge_service import create_lounge, list_lounges
from backend.models import get_db
from backend.dependencies.auth import get_current_user

router = APIRouter(prefix="/lounge", tags=["lounge"])

@router.post("/", response_model=LoungeOut)
def create(data: LoungeCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    return create_lounge(db, community_id=data.community_id, name=data.name, description=data.description)

@router.get("/", response_model=list[LoungeOut])
def list_all(community_id: int | None = None, db: Session = Depends(get_db)):
    return list_lounges(db, community_id=community_id)

