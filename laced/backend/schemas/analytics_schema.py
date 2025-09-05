# schemas/analytics_schema.py

from pydantic import BaseModel
from typing import Dict


class UsageStatsOut(BaseModel):
    active_users: int
    total_images: int
    total_videos: int
    other_metrics: Dict[str, int]


class GrowthMetricsOut(BaseModel):
    new_users: int
    growth_percentage: float
