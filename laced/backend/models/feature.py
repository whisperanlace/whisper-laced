# models/Feature.py
from sqlalchemy import Column, Integer, String, Boolean, DateTime, Text
from app.database import Base
from datetime import datetime

class Feature(Base):
    __tablename__ = "features"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(128), unique=True, nullable=False)
    description = Column(Text, nullable=True)
    enabled = Column(Boolean, default=False, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
