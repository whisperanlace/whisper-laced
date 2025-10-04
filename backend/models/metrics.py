from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from .base import Base

class Metrics(Base):
    __tablename__ = "metrics"

    id = Column(Integer, primary_key=True, index=True)
    event_type = Column(String, nullable=False)
    value = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)

