from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.schemas.motion_schema import MotionCreate, MotionOut
from backend.services.motion_service import create_motion
from backend.models import get_db
from backend.dependencies.auth import get_current_user

router = APIRouter(prefix="/motion", tags=["motion"])

@router.post("/", response_model=MotionOut)
def create(data: MotionCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    return create_motion(db, created_by=user.id, title=data.title, description=data.description, community_id=data.community_id, lounge_id=data.lounge_id)

