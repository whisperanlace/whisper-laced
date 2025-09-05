# controllers/enhancement_request_controller.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.enhancement_request_schema import EnhancementRequestCreate, EnhancementRequestOut
from services.enhancement_request_service import EnhancementRequestService
from utils.dependencies import get_db, get_current_user

router = APIRouter(prefix="/enhancements", tags=["Enhancement Requests"])


@router.post("/", response_model=EnhancementRequestOut)
def create_request(
    req: EnhancementRequestCreate,
    db: Session = Depends(get_db),
    user=Depends(get_current_user),
):
    return EnhancementRequestService.create_request(db, user.id, req)


@router.get("/", response_model=list[EnhancementRequestOut])
def list_requests(db: Session = Depends(get_db)):
    return EnhancementRequestService.list_requests(db)
