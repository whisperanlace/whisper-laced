from fastapi import APIRouter, Depends, HTTPException
from backend.controllers.premium_controller import PremiumController
from backend.schemas.premium_schema import PremiumSchema
from backend.utils.dependencies import get_current_user

router = APIRouter()
premium_ctrl = PremiumController()

@router.get("/", response_model=PremiumSchema)
async def get_premium_status(current_user=Depends(get_current_user)):
    return await premium_ctrl.get_status(current_user)

@router.post("/upgrade", response_model=PremiumSchema)
async def upgrade_premium(current_user=Depends(get_current_user)):
    try:
        return await premium_ctrl.upgrade(current_user)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
