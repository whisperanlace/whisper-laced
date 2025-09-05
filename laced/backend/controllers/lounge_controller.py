# controllers/lounge_controller.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.room_schema import RoomOut
from services.lounge_service import LoungeService
from utils.dependencies import get_db, get_current_user

router = APIRouter(prefix="/lounge", tags=["Lounge"])


@router.get("/", response_model=list[RoomOut])
def get_lounge_rooms(db: Session = Depends(get_db), user=Depends(get_current_user)):
    return LoungeService.get_public_rooms(db)
