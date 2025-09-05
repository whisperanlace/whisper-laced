# models/Post.py
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from app.database import Base
from datetime import datetime

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="SET NULL"), nullable=True, index=True)
    community_id = Column(Integer, ForeignKey("communities.id", ondelete="SET NULL"), nullable=True, index=True)
    title = Column(String(255), nullable=True)
    content = Column(Text, nullable=True)
    content_type = Column(String(32), default="text", nullable=False)
    is_published = Column(Boolean, default=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=True)

    owner = relationship("User", back_populates="posts")
    community = relationship("Community", back_populates="posts")
    comments = relationship("Comment", back_populates="post", cascade="all, delete-orphan")
    images = relationship("Image", back_populates="post", cascade="all, delete-orphan")
    videos = relationship("Video", back_populates="post", cascade="all, delete-orphan")
    collections = relationship("Collection", secondary="collection_posts", back_populates="posts")
