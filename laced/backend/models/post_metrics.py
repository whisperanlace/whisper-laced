# models/Post_metrics.py
from sqlalchemy import Column, Integer, DateTime, ForeignKey
from app.database import Base
from datetime import datetime

class PostMetrics(Base):
    __tablename__ = "post_metrics"

    id = Column(Integer, primary_key=True, index=True)
    post_id = Column(Integer, ForeignKey("posts.id", ondelete="CASCADE"), nullable=False, index=True)
    views = Column(Integer, default=0, nullable=False)
    likes = Column(Integer, default=0, nullable=False)
    shares = Column(Integer, default=0, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
