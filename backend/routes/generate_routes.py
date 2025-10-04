from __future__ import annotations
from typing import Any, Dict
from fastapi import APIRouter, Depends
from pydantic import BaseModel, Field
from celery.result import AsyncResult

from backend.celery_app import app as celery_app
from backend.tasks.generate import generate_image_task
from backend.security.auth import auth_bearer
from backend.routes.metrics_routes import ENQUEUES, POLLS

router = APIRouter(
    prefix="/generate",
    tags=["generate"],
    dependencies=[Depends(auth_bearer)],
)

class GenerateRequest(BaseModel):
    prompt: str = Field(..., min_length=1)
    params: Dict[str, Any] = Field(default_factory=dict)

@router.post("", summary="Enqueue a generation job")
def enqueue(req: GenerateRequest):
    ENQUEUES.inc()
    asyncres = generate_image_task.delay(req.prompt, **req.params)
    return {"task_id": asyncres.id}

@router.get("/{task_id}", summary="Check generation status/result")
def status(task_id: str):
    POLLS.inc()
    r = AsyncResult(task_id, app=celery_app)
    return {
        "id": task_id,
        "status": r.status,
        "ready": r.ready(),
        "result": r.result if r.ready() else None,
    }