# -*- coding: utf-8 -*-
import pytest
from config.celery_config import celery_app

@pytest.mark.asyncio
async def test_celery_jobs():
    # Dummy task to ensure celery is running
    result = celery_app.send_task("jobs.cleanup_job")
    assert result.id is not None
