# services/Webhook_service.py
from sqlalchemy.orm import Session
from app.models.Webhook import Webhook
from fastapi import HTTPException, status

class WebhookService:
    async def register_webhook(self, db: Session, url: str, event: str):
        webhook = Webhook(url=url, event=event)
        db.add(webhook)
        db.commit()
        db.refresh(webhook)
        return webhook

    async def list_webhooks(self, db: Session):
        return db.query(Webhook).all()
