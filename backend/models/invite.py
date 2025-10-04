from __future__ import annotations
from datetime import datetime
from enum import Enum
from sqlalchemy import Integer, String, ForeignKey, DateTime, Enum as SQLEnum, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base


class InviteStatus(str, Enum):
    PENDING = "pending"
    ACCEPTED = "accepted"
    DECLINED = "declined"
    EXPIRED = "expired"


class Invite(Base):
    __tablename__ = "invites"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    sender_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id", ondelete="CASCADE"), index=True)
    recipient_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id", ondelete="CASCADE"), index=True)
    community_id: Mapped[int | None] = mapped_column(Integer, ForeignKey("communities.id", ondelete="CASCADE"), nullable=True)

    message: Mapped[str | None] = mapped_column(String(255), nullable=True)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    status: Mapped[InviteStatus] = mapped_column(SQLEnum(InviteStatus), default=InviteStatus.PENDING, nullable=False)

    # Relationships
    sender = relationship("User", foreign_keys=[sender_id], backref="sent_invites")
    recipient = relationship("User", foreign_keys=[recipient_id], backref="received_invites")
    community = relationship("Community", back_populates="invites")
