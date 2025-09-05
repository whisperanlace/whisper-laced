# services/Post_metrics_service.py
from sqlalchemy.orm import Session
from app.models.Post_metrics import PostMetrics

class PostMetricsService:
    async def log_metrics(self, db: Session, post_id: int, views: int, likes: int):
        metrics = PostMetrics(post_id=post_id, views=views, likes=likes)
        db.add(metrics)
        db.commit()
        db.refresh(metrics)
        return metrics
