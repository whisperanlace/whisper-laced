# controllers/invite_controller.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.invite_schema import InviteCreate, InviteOut
from services.invite_service import InviteService
from utils.dependencies import get_db, get_current_user

router = APIRouter(prefix="/invites", tags=["Invites"])


@router.post("/", response_model=InviteOut)
def create_invite(
    invite: InviteCreate, db: Session = Depends(get_db), user=Depends(get_current_user)
):
    if not user.is_admin:
        raise HTTPException(status_code=403, detail="Unauthorized")
    return InviteService.create_invite(db, user.id, invite)


@router.get("/", response_model=list[InviteOut])
def list_invites(db: Session = Depends(get_db), user=Depends(get_current_user)):
    if not user.is_admin:
        raise HTTPException(status_code=403, detail="Unauthorized")
    return InviteService.list_invites(db)
