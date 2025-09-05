# models/Tier.py
from sqlalchemy import Column, Integer, String, Float, Text, DateTime
from app.database import Base
from datetime import datetime

class Tier(Base):
    __tablename__ = "tiers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(128), nullable=False, unique=True)
    price = Column(Float, default=0.0, nullable=False)
    benefits = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
