from __future__ import annotations
from sqlalchemy.orm import Session
from sqlalchemy import select, func
from typing import List, Optional
from backend.models import EditorDocument, EnhancementVersion

def create_document(db: Session, owner_id: int, title: str, media_id: int | None) -> EditorDocument:
    doc = EditorDocument(owner_id=owner_id, title=title, media_id=media_id)
    db.add(doc)
    db.flush()
    # initial version 1 (optional)
    v = EnhancementVersion(document_id=doc.id, version_index=1, notes="Initial")
    db.add(v)
    db.commit()
    db.refresh(doc)
    return doc

def list_documents(db: Session, owner_id: int, limit: int = 50, offset: int = 0) -> list[EditorDocument]:
    q = db.execute(select(EditorDocument).where(EditorDocument.owner_id == owner_id).order_by(EditorDocument.id.desc()).limit(limit).offset(offset))
    return [r[0] for r in q.all()]

def get_document(db: Session, doc_id: int, owner_id: int) -> Optional[EditorDocument]:
    q = db.execute(select(EditorDocument).where(EditorDocument.id == doc_id, EditorDocument.owner_id == owner_id))
    row = q.first()
    return row[0] if row else None

def next_version_index(db: Session, doc_id: int) -> int:
    q = db.execute(select(func.max(EnhancementVersion.version_index)).where(EnhancementVersion.document_id == doc_id))
    maxv = q.scalar()
    return (maxv or 0) + 1

def save_version(db: Session, doc_id: int, request_id: int | None, url: str | None, notes: str | None) -> EnhancementVersion:
    v = EnhancementVersion(
        document_id=doc_id,
        parent_request_id=request_id,
        version_index=next_version_index(db, doc_id),
        url=url,
        notes=notes,
    )
    db.add(v)
    db.commit()
    db.refresh(v)
    return v

def list_versions(db: Session, doc_id: int) -> list[EnhancementVersion]:
    q = db.execute(select(EnhancementVersion).where(EnhancementVersion.document_id == doc_id).order_by(EnhancementVersion.version_index.asc()))
    return [r[0] for r in q.all()]

