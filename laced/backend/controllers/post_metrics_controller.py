from fastapi import HTTPException
from backend.services.post_metrics_service import PostMetricsService

post_metrics_service = PostMetricsService()

class PostMetricsController:

    async def get_metrics(self, post_id: str):
        try:
            return await post_metrics_service.get_metrics(post_id)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
