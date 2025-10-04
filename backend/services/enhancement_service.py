from __future__ import annotations
from sqlalchemy.orm import Session
from sqlalchemy import select
from typing import Optional
from backend.models import EnhancementRequest
from backend.services.editor_service import save_version

def create_request(db: Session, document_id: int, requested_by: int, prompt: str) -> EnhancementRequest:
    r = EnhancementRequest(document_id=document_id, requested_by=requested_by, prompt=prompt, status="queued")
    db.add(r)
    db.flush()
    return r

def process_request_immediate(db: Session, req: EnhancementRequest) -> EnhancementRequest:
    # Simulate enhancement done: create a new version with simple note
    req.status = "done"
    v = save_version(db, doc_id=req.document_id, request_id=req.id, url=None, notes=f"Enhanced: {req.prompt}")
    db.commit()
    return req

