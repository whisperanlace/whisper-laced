# controllers/analytics_controller.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from services.analytics_service import AnalyticsService
from utils.dependencies import get_db, get_current_user

router = APIRouter(prefix="/analytics", tags=["Analytics"])


@router.get("/usage")
def get_usage(db: Session = Depends(get_db), user=Depends(get_current_user)):
    if not user.is_admin:
        return {"detail": "Unauthorized"}
    return AnalyticsService.get_usage_stats(db)


@router.get("/growth")
def get_growth(db: Session = Depends(get_db), user=Depends(get_current_user)):
    if not user.is_admin:
        return {"detail": "Unauthorized"}
    return AnalyticsService.get_growth_metrics(db)
