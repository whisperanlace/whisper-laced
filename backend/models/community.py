from __future__ import annotations
from datetime import datetime
from sqlalchemy import Integer, String, DateTime, ForeignKey, Table, Column, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base

# ✅ Association table for Users <-> Communities
community_members = Table(
    "community_members",
    Base.metadata,
    Column("user_id", Integer, ForeignKey("users.id", ondelete="CASCADE"), primary_key=True),
    Column("community_id", Integer, ForeignKey("communities.id", ondelete="CASCADE"), primary_key=True),
)

class Community(Base):
    __tablename__ = "communities"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    description: Mapped[str | None] = mapped_column(String(255), nullable=True)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    # Relationships
    lounges = relationship("Lounge", back_populates="community", cascade="all, delete-orphan")
    posts = relationship("Post", back_populates="community", cascade="all, delete-orphan")
    invites = relationship("Invite", back_populates="community", cascade="all, delete-orphan")

    # ✅ Many-to-Many: Communities <-> Users
    members = relationship(
        "User",
        secondary=community_members,
        backref="communities",
        cascade="all, delete"
    )
