from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Optional, Dict, Any

from sqlalchemy import (
    Column, Integer, String, Enum as SAEnum, Boolean, ForeignKey, DateTime, JSON, Index
)
from sqlalchemy.orm import relationship

from .base import Base


class TargetType(str, Enum):
    media = "media"
    video = "video"
    post = "post"
    comment = "comment"
    profile = "profile"


class ModerationStatus(str, Enum):
    pending = "pending"
    approved = "approved"
    rejected = "rejected"
    escalated = "escalated"


class ModerationCase(Base):
    __tablename__ = "moderation_cases"

    id = Column(Integer, primary_key=True, index=True)
    target_type = Column(SAEnum(TargetType), nullable=False, index=True)
    target_id = Column(Integer, nullable=False, index=True)
    status = Column(SAEnum(ModerationStatus), nullable=False, default=ModerationStatus.pending, index=True)
    reason = Column(String(255), nullable=True)
    detected_labels = Column(JSON, nullable=True)
    is_nsfw = Column(Boolean, default=False, nullable=False)

    created_by_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    assigned_to_id = Column(Integer, ForeignKey("users.id"), nullable=True)

    resolution_notes = Column(String(2000), nullable=True)

    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    created_by = relationship("User", foreign_keys=[created_by_id])
    assigned_to = relationship("User", foreign_keys=[assigned_to_id])

    reports = relationship("Report", back_populates="moderation_case", cascade="all,delete-orphan")

    __table_args__ = (
        Index("ix_moderation_target", "target_type", "target_id", unique=False),
    )

