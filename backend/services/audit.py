from backend.models import AuditLog
from sqlalchemy.orm import Session

def log(db: Session, *, actor:str|None, action:str, target:str|None=None, ip:str|None=None, ua:str|None=None, meta:str|None=None):
    entry = AuditLog(actor=actor, action=action, target=target, ip=ip, user_agent=ua, meta=meta)
    db.add(entry); db.commit()

