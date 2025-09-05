# models/Video.py
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base
from datetime import datetime

class Video(Base):
    __tablename__ = "videos"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="SET NULL"), nullable=True, index=True)
    post_id = Column(Integer, ForeignKey("posts.id", ondelete="CASCADE"), nullable=True, index=True)
    lora_id = Column(Integer, ForeignKey("loras.id", ondelete="SET NULL"), nullable=True)
    filename = Column(String(512), nullable=False)
    url = Column(String(1024), nullable=False)
    mime_type = Column(String(128), nullable=True)
    duration_seconds = Column(Integer, nullable=True)
    filesize = Column(Integer, nullable=True)
    thumbnail_url = Column(String(1024), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    user = relationship("User", back_populates="videos")
    post = relationship("Post", back_populates="videos")
    lora = relationship("Lora", back_populates="videos")
