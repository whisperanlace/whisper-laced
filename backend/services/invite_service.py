import secrets
from datetime import datetime, timezone
from sqlalchemy.orm import Session
from backend.models import Invite, InviteStatus

def create_invite(db: Session, inviter_id: int, invitee_email: str, community_id: int | None, lounge_id: int | None) -> Invite:
    token = secrets.token_urlsafe(24)
    inv = Invite(inviter_id=inviter_id, invitee_email=invitee_email, token=token, community_id=community_id, lounge_id=lounge_id)
    db.add(inv)
    db.commit()
    db.refresh(inv)
    return inv

def accept_invite(db: Session, token: str) -> Invite | None:
    inv = db.query(Invite).filter(Invite.token == token, Invite.status == InviteStatus.pending).first()
    if not inv:
        return None
    inv.status = InviteStatus.accepted
    inv.accepted_at = datetime.now(timezone.utc)
    db.add(inv)
    db.commit()
    db.refresh(inv)
    return inv

