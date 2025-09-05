from fastapi import HTTPException
from backend.services.webhook_service import WebhookService

webhook_service = WebhookService()

class WebhookController:

    async def register_webhook(self, payload, current_user):
        try:
            return await webhook_service.register(payload, current_user)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    async def delete_webhook(self, webhook_id: str, current_user):
        success = await webhook_service.delete_webhook(webhook_id, current_user)
        if not success:
            raise HTTPException(status_code=400, detail="Could not delete webhook")
