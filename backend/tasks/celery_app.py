import os
from celery import Celery

BROKER_URL  = os.getenv("CELERY_BROKER_URL",  "redis://redis:6379/0")
BACKEND_URL = os.getenv("CELERY_RESULT_BACKEND", "redis://redis:6379/1")

app = Celery("whisper-laced", broker=BROKER_URL, backend=BACKEND_URL, include=[
    "backend.tasks.image_tasks",
    "backend.tasks.video_tasks",
    "backend.tasks.upload_tasks",
    "backend.tasks.notification_tasks",
    "backend.tasks.moderation_tasks",
])

app.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone=os.getenv("TZ", "UTC"),
    enable_utc=True,
    task_time_limit=600,
    task_soft_time_limit=540,
    worker_prefetch_multiplier=1,
)
