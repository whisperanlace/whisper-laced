# models/Room.py
from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base
from datetime import datetime

class Room(Base):
    __tablename__ = "rooms"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    topic = Column(String(255), nullable=True)
    community_id = Column(Integer, ForeignKey("communities.id", ondelete="CASCADE"), nullable=True, index=True)
    creator_id = Column(Integer, ForeignKey("users.id", ondelete="SET NULL"), nullable=True, index=True)
    is_private = Column(Boolean, default=False, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    community = relationship("Community", back_populates="rooms")
    creator = relationship("User", back_populates="rooms")
    messages = relationship("Message", back_populates="room", cascade="all, delete-orphan")
