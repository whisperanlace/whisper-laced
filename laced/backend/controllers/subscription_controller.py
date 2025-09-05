# controllers/subscription_controller.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.subscription_schema import SubscriptionCreate, SubscriptionOut
from services.subscription_service import SubscriptionService
from utils.dependencies import get_db, get_current_user

router = APIRouter(prefix="/subscriptions", tags=["Subscriptions"])


@router.post("/", response_model=SubscriptionOut)
def create_subscription(
    sub: SubscriptionCreate,
    db: Session = Depends(get_db),
    user=Depends(get_current_user),
):
    return SubscriptionService.create_subscription(db, user.id, sub)


@router.get("/", response_model=list[SubscriptionOut])
def list_subscriptions(
    db: Session = Depends(get_db), user=Depends(get_current_user)
):
    return SubscriptionService.list_user_subscriptions(db, user.id)


@router.delete("/{subscription_id}")
def cancel_subscription(
    subscription_id: int,
    db: Session = Depends(get_db),
    user=Depends(get_current_user),
):
    success = SubscriptionService.cancel_subscription(db, subscription_id, user.id)
    if not success:
        raise HTTPException(status_code=404, detail="Subscription not found")
    return {"detail": "Subscription cancelled"}
