# models/Report.py
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base
from datetime import datetime

class Report(Base):
    __tablename__ = "reports"

    id = Column(Integer, primary_key=True, index=True)
    reporter_id = Column(Integer, ForeignKey("users.id", ondelete="SET NULL"), nullable=True, index=True)
    target_type = Column(String(64), nullable=False)
    target_id = Column(Integer, nullable=False)
    reason = Column(Text, nullable=True)
    status = Column(String(32), default="open", nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    reporter = relationship("User")
