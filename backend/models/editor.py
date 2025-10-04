from __future__ import annotations
from sqlalchemy import Column, Integer, String, ForeignKey, Text, DateTime, func
from sqlalchemy.orm import relationship
from .base import Base

class EditorDocument(Base):
    __tablename__ = "editor_documents"
    id = Column(Integer, primary_key=True, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)
    title = Column(String(255), nullable=False)
    media_id = Column(Integer, nullable=True)  # optional link to existing media/upload id
    created_at = Column(DateTime, nullable=False, server_default=func.now())
    updated_at = Column(DateTime, nullable=False, server_default=func.now(), onupdate=func.now())

    enhancements = relationship("EnhancementRequest", back_populates="document", cascade="all,delete-orphan")
    versions = relationship("EnhancementVersion", back_populates="document", cascade="all,delete-orphan")

class EnhancementRequest(Base):
    __tablename__ = "enhancement_requests"
    id = Column(Integer, primary_key=True, index=True)
    document_id = Column(Integer, ForeignKey("editor_documents.id"), nullable=False, index=True)
    requested_by = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)
    prompt = Column(Text, nullable=False)
    status = Column(String(32), nullable=False, default="queued")  # queued|processing|done|failed
    created_at = Column(DateTime, nullable=False, server_default=func.now())

    document = relationship("EditorDocument", back_populates="enhancements")

class EnhancementVersion(Base):
    __tablename__ = "enhancement_versions"
    id = Column(Integer, primary_key=True, index=True)
    document_id = Column(Integer, ForeignKey("editor_documents.id"), nullable=False, index=True)
    parent_request_id = Column(Integer, ForeignKey("enhancement_requests.id"), nullable=True)
    version_index = Column(Integer, nullable=False, default=1)
    url = Column(String(2048), nullable=True)    # where the new asset lives (could be file path or URL)
    notes = Column(Text, nullable=True)
    created_at = Column(DateTime, nullable=False, server_default=func.now())

    document = relationship("EditorDocument", back_populates="versions")


