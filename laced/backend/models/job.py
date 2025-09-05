# models/Job.py
from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean
from app.database import Base
from datetime import datetime

class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    task_type = Column(String(128), nullable=False)
    payload = Column(Text, nullable=True)  # JSON string
    status = Column(String(32), default="pending", nullable=False)
    scheduled_at = Column(DateTime, nullable=True)
    started_at = Column(DateTime, nullable=True)
    completed_at = Column(DateTime, nullable=True)
    attempts = Column(Integer, default=0, nullable=False)
    last_error = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
