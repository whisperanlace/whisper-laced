from fastapi import HTTPException
from backend.services.billing_service import BillingService

billing_service = BillingService()

class BillingController:

    async def get_billing_info(self, current_user):
        return await billing_service.get_billing_info(current_user)

    async def create_invoice(self, payload, current_user):
        try:
            return await billing_service.create_invoice(payload, current_user)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    async def pay_invoice(self, invoice_id: str, current_user):
        success = await billing_service.pay_invoice(invoice_id, current_user)
        if not success:
            raise HTTPException(status_code=400, detail="Payment failed")
