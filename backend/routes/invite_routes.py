from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.schemas.invite_schema import InviteCreate, InviteOut, InviteAccept
from backend.services.invite_service import create_invite, accept_invite
from backend.models import get_db
from backend.dependencies.auth import get_current_user

router = APIRouter(prefix="/invite", tags=["invite"])

@router.post("/", response_model=InviteOut)
def create(data: InviteCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    if not data.community_id and not data.lounge_id:
        raise HTTPException(status_code=400, detail="community_id or lounge_id required")
    return create_invite(db, inviter_id=user.id, invitee_email=data.invitee_email, community_id=data.community_id, lounge_id=data.lounge_id)

@router.post("/accept", response_model=InviteOut)
def accept(data: InviteAccept, db: Session = Depends(get_db)):
    inv = accept_invite(db, token=data.token)
    if not inv:
        raise HTTPException(status_code=404, detail="Invite not found or already used")
    return inv

