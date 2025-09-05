# models/Lora.py
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from app.database import Base
from datetime import datetime

class Lora(Base):
    __tablename__ = "loras"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="SET NULL"), nullable=True, index=True)
    name = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    filename = Column(String(512), nullable=False)
    path = Column(String(2048), nullable=False)
    verified = Column(Boolean, default=False, nullable=False)
    version = Column(String(64), nullable=True)
    metadata = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    verified_at = Column(DateTime, nullable=True)

    user = relationship("User", back_populates="loras")
    images = relationship("Image", back_populates="lora", cascade="all, delete-orphan")
    videos = relationship("Video", back_populates="lora", cascade="all, delete-orphan")
    avatars = relationship("Avatar", back_populates="lora", cascade="all, delete-orphan")
    upload_logs = relationship("LoraUploadLog", back_populates="lora", cascade="all, delete-orphan")
