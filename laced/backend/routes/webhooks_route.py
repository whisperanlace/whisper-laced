from fastapi import APIRouter, Request, HTTPException
from backend.controllers.webhook_controller import WebhookController

router = APIRouter()
webhook_ctrl = WebhookController()

@router.post("/{webhook_name}")
async def handle_webhook(webhook_name: str, request: Request):
    payload = await request.json()
    try:
        return await webhook_ctrl.handle(webhook_name, payload)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
