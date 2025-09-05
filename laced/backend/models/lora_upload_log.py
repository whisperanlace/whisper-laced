# models/Lora_upload_log.py
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean, Text
from sqlalchemy.orm import relationship
from app.database import Base
from datetime import datetime

class LoraUploadLog(Base):
    __tablename__ = "lora_upload_logs"

    id = Column(Integer, primary_key=True, index=True)
    lora_id = Column(Integer, ForeignKey("loras.id", ondelete="CASCADE"), nullable=False, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="SET NULL"), nullable=True, index=True)
    filename = Column(String(512), nullable=True)
    status = Column(String(64), default="uploaded", nullable=False)
    verified = Column(Boolean, default=False, nullable=False)
    message = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    lora = relationship("Lora", back_populates="upload_logs")
    user = relationship("User")
