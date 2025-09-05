# models/Subscription.py
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean, Float
from sqlalchemy.orm import relationship
from app.database import Base
from datetime import datetime

class Subscription(Base):
    __tablename__ = "subscriptions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    tier = Column(String(64), nullable=False)  # standard, premium, deluxe
    active = Column(Boolean, default=True, nullable=False)
    start_date = Column(DateTime, default=datetime.utcnow, nullable=False)
    end_date = Column(DateTime, nullable=True)
    recurring_amount = Column(Float, nullable=True)
    currency = Column(String(8), default="USD", nullable=True)

    user = relationship("User")
