from fastapi import APIRouter, Depends, HTTPException
from backend.controllers.subscription_controller import SubscriptionController
from backend.schemas.subscription_schema import SubscriptionSchema
from backend.utils.dependencies import get_current_user
from typing import List

router = APIRouter()
sub_ctrl = SubscriptionController()

@router.get("/", response_model=List[SubscriptionSchema])
async def list_subscriptions(current_user=Depends(get_current_user)):
    return await sub_ctrl.list_subscriptions(current_user)

@router.post("/", response_model=SubscriptionSchema)
async def subscribe(payload: SubscriptionSchema, current_user=Depends(get_current_user)):
    try:
        return await sub_ctrl.subscribe(payload, current_user)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/{subscription_id}", status_code=204)
async def unsubscribe(subscription_id: str, current_user=Depends(get_current_user)):
    await sub_ctrl.unsubscribe(subscription_id, current_user)
    return {"detail": "Deleted"}
