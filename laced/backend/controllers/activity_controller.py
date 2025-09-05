# controllers/activity_controller.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from services.activity_service import ActivityService
from utils.dependencies import get_db, get_current_user

router = APIRouter(prefix="/activity", tags=["Activity"])


@router.get("/")
def get_user_activity(db: Session = Depends(get_db), user=Depends(get_current_user)):
    return ActivityService.get_user_activity(db, user.id)
