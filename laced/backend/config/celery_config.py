# -*- coding: utf-8 -*-
"""
Celery configuration for Laced backend.
Broker, backend, serialization, and timezone settings.
"""

from celery import Celery
from .settings import settings

celery_app = Celery(
    "laced",
    broker=settings.CELERY_BROKER_URL,
    backend=settings.CELERY_RESULT_BACKEND,
)

celery_app.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="UTC",
    enable_utc=True,
    broker_connection_retry_on_startup=True,
)

# Automatically discover tasks in jobs/
celery_app.autodiscover_tasks(packages=["jobs"])
