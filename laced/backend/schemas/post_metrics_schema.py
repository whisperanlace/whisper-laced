# schemas/post_metrics_schema.py

from pydantic import BaseModel


class PostMetricsOut(BaseModel):
    post_id: int
    views: int
    likes: int
    comments: int
    shares: int
