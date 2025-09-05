# controllers/post_metrics_controller.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from services.post_metrics_service import PostMetricsService
from utils.dependencies import get_db, get_current_user

router = APIRouter(prefix="/post-metrics", tags=["Post Metrics"])


@router.get("/{post_id}")
def get_post_metrics(
    post_id: int, db: Session = Depends(get_db), user=Depends(get_current_user)
):
    return PostMetricsService.get_post_metrics(db, post_id)
