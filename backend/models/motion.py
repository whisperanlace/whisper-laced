from __future__ import annotations
from datetime import datetime
from sqlalchemy import Integer, String, ForeignKey, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base


class Motion(Base):
    __tablename__ = "motions"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    lounge_id: Mapped[int] = mapped_column(Integer, ForeignKey("lounges.id", ondelete="CASCADE"), index=True)
    description: Mapped[str] = mapped_column(String(255), nullable=False)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())

    # Relationships
    lounge = relationship("Lounge", backref="motions")
