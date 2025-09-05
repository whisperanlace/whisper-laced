from fastapi import APIRouter, Depends, HTTPException
from typing import List
from backend.controllers.feedback_controller import FeedbackController
from backend.schemas.feedback_schema import FeedbackSchema
from backend.utils.dependencies import get_current_user

router = APIRouter()
feedback_ctrl = FeedbackController()

@router.post("/", response_model=FeedbackSchema)
async def submit_feedback(payload: FeedbackSchema, current_user=Depends(get_current_user)):
    try:
        return await feedback_ctrl.submit_feedback(payload, current_user)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/", response_model=List[FeedbackSchema])
async def list_feedback(current_user=Depends(get_current_user)):
    return await feedback_ctrl.list_feedback(current_user)
