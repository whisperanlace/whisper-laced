from fastapi import APIRouter, Depends, HTTPException
from backend.controllers.moderation_controller import ModerationController
from backend.schemas.moderation_schema import ModerationSchema
from backend.utils.dependencies import get_current_user

router = APIRouter()
mod_ctrl = ModerationController()

@router.post("/review", response_model=ModerationSchema)
async def review_content(content_id: str, current_user=Depends(get_current_user)):
    try:
        return await mod_ctrl.review_content(content_id, current_user)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
