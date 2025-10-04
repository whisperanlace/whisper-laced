from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, func
from sqlalchemy.orm import relationship
from .base import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False, index=True)
    email = Column(String, unique=True, nullable=False, index=True)
    hashed_password = Column(String, nullable=False)

    tier_id = Column(Integer, ForeignKey("tiers.id"), nullable=True)
    tier = relationship("Tier", back_populates="users")

    # Phase 5 relationships
    loras   = relationship("LoRA",   back_populates="user", cascade="all, delete-orphan")
    avatars = relationship("Avatar", back_populates="user", cascade="all, delete-orphan")
    uploads = relationship("Upload", back_populates="user", cascade="all, delete-orphan")
    videos  = relationship("Video",  back_populates="user", cascade="all, delete-orphan")
    media   = relationship("Media",  back_populates="user", cascade="all, delete-orphan")

    # NEW: history relationship (Fix for current error)
    history = relationship("History", back_populates="user", cascade="all, delete-orphan")

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    api_key = Column(String, nullable=True)

