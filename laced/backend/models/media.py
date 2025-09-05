# models/Media.py
from sqlalchemy import Column, Integer, String, DateTime, Text
from app.database import Base
from datetime import datetime

class Media(Base):
    __tablename__ = "media"

    id = Column(Integer, primary_key=True, index=True)
    owner_type = Column(String(64), nullable=True)  # user, post, community
    owner_id = Column(Integer, nullable=True)
    media_type = Column(String(32), nullable=False)  # image, video, avatar
    filename = Column(String(512), nullable=False)
    url = Column(String(1024), nullable=False)
    metadata = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
