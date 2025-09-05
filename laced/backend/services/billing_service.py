# services/Billing_service.py
from sqlalchemy.orm import Session
from app.models.Billing import Billing

class BillingService:
    async def create_invoice(self, db: Session, user_id: int, amount: float):
        billing = Billing(user_id=user_id, amount=amount)
        db.add(billing)
        db.commit()
        db.refresh(billing)
        return billing
