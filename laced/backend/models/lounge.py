# models/Lounge.py
from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime
from app.database import Base
from datetime import datetime

class Lounge(Base):
    __tablename__ = "lounges"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    is_private = Column(Boolean, default=False, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
