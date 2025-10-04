from __future__ import annotations
from datetime import datetime
from sqlalchemy import Integer, String, DateTime, ForeignKey, Table, Column, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base

# ✅ Association table for Users <-> Lounges
lounge_members = Table(
    "lounge_members",
    Base.metadata,
    Column("user_id", Integer, ForeignKey("users.id", ondelete="CASCADE"), primary_key=True),
    Column("lounge_id", Integer, ForeignKey("lounges.id", ondelete="CASCADE"), primary_key=True),
)

class Lounge(Base):
    __tablename__ = "lounges"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    community_id: Mapped[int] = mapped_column(Integer, ForeignKey("communities.id", ondelete="CASCADE"), index=True)

    name: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str | None] = mapped_column(String(255), nullable=True)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    # Relationships
    community = relationship("Community", back_populates="lounges")

    members = relationship(
        "User",
        secondary=lounge_members,
        backref="lounges",
        cascade="all, delete"
    )

    posts = relationship("Post", back_populates="lounge", cascade="all, delete-orphan")
