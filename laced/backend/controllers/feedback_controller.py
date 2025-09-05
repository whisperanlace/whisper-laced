from fastapi import APIRouter, Depends
from backend.services import FeedbackService
from backend.schemas.feedback_schema import FeedbackSchema
from backend.utils.dependencies import get_current_user

router = APIRouter(prefix="/feedback", tags=["Feedback"])
feedback_service = FeedbackService()

@router.post("/")
async def submit_feedback(payload: FeedbackSchema, user=Depends(get_current_user)):
    return await feedback_service.submit_feedback(payload, user)

@router.get("/")
async def get_feedback(user=Depends(get_current_user)):
    return await feedback_service.get_feedback(user)
