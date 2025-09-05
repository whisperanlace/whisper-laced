# controllers/premium_controller.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from services.premium_service import PremiumService
from utils.dependencies import get_db, get_current_user

router = APIRouter(prefix="/premium", tags=["Premium"])


@router.get("/status")
def get_premium_status(db: Session = Depends(get_db), user=Depends(get_current_user)):
    return PremiumService.get_status(db, user.id)


@router.post("/upgrade")
def upgrade_to_premium(db: Session = Depends(get_db), user=Depends(get_current_user)):
    return PremiumService.upgrade_user(db, user.id)
