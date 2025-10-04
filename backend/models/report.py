from __future__ import annotations

from datetime import datetime
from enum import Enum
from sqlalchemy import Column, Integer, String, Enum as SAEnum, ForeignKey, DateTime, Text
from sqlalchemy.orm import relationship

from .base import Base
from .moderation import TargetType


class ReportStatus(str, Enum):
    open = "open"
    merged = "merged"
    closed = "closed"


class ReportReason(str, Enum):
    nsfw = "NSFW"
    spam = "SPAM"
    abuse = "ABUSE"
    copyright = "COPYRIGHT"
    other = "OTHER"


class Report(Base):
    __tablename__ = "reports"

    id = Column(Integer, primary_key=True, index=True)
    reporter_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    target_type = Column(SAEnum(TargetType), nullable=False, index=True)
    target_id = Column(Integer, nullable=False, index=True)
    reason = Column(SAEnum(ReportReason), nullable=False)
    details = Column(Text, nullable=True)
    status = Column(SAEnum(ReportStatus), nullable=False, default=ReportStatus.open, index=True)

    moderation_case_id = Column(Integer, ForeignKey("moderation_cases.id"), nullable=True)

    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    reporter = relationship("User", foreign_keys=[reporter_id])
    moderation_case = relationship("ModerationCase", back_populates="reports")



