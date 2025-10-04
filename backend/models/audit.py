from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Text
from .base import Base

class AuditLog(Base):
    __tablename__ = "audit_logs"
    id = Column(Integer, primary_key=True)
    actor = Column(String(255), nullable=True)  # user email / system
    action = Column(String(128), nullable=False)
    target = Column(String(255), nullable=True)
    ip = Column(String(64), nullable=True)
    user_agent = Column(String(255), nullable=True)
    meta = Column(Text, nullable=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)


