from __future__ import annotations
from celery import Celery
from backend.config import settings

def make_celery() -> Celery:
    app = Celery(
        "backend",
        broker=settings.CELERY_BROKER_URL,
        backend=settings.CELERY_RESULT_BACKEND,
        include=[
            "backend.tasks.generate",
            "backend.tasks.notifications",
            "backend.tasks.moderation_tasks",
        ],
    )
    app.conf.update(
        imports=("backend.tasks.generate",),
        task_serializer="json",
        accept_content=["json"],
        result_serializer="json",
        timezone="UTC",
        enable_utc=True,
    )
    return app

app: Celery = make_celery()
celery: Celery = app
__all__ = ["app", "celery"]