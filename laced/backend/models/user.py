# models/User.py
from sqlalchemy import Column, Integer, String, Boolean, DateTime, Text
from sqlalchemy.orm import relationship
from app.database import Base
from datetime import datetime

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, nullable=False, index=True)
    username = Column(String(64), unique=True, nullable=False, index=True)
    display_name = Column(String(128), nullable=True)
    hashed_password = Column(String(255), nullable=False)
    bio = Column(Text, nullable=True)
    is_active = Column(Boolean, default=True, nullable=False)
    is_admin = Column(Boolean, default=False, nullable=False)
    role = Column(String(50), default="user", nullable=False)
    subscription_tier = Column(String(50), default="standard", nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    # Relationships
    posts = relationship("Post", back_populates="owner", cascade="all, delete-orphan")
    comments = relationship("Comment", back_populates="user", cascade="all, delete-orphan")
    images = relationship("Image", back_populates="user", cascade="all, delete-orphan")
    videos = relationship("Video", back_populates="user", cascade="all, delete-orphan")
    avatars = relationship("Avatar", back_populates="user", cascade="all, delete-orphan")
    loras = relationship("Lora", back_populates="user", cascade="all, delete-orphan")
    sessions = relationship("Session", back_populates="user", cascade="all, delete-orphan")
    notifications = relationship("Notification", back_populates="user", cascade="all, delete-orphan")
    feedbacks = relationship("Feedback", back_populates="user", cascade="all, delete-orphan")
    reactions = relationship("Reaction", back_populates="user", cascade="all, delete-orphan")
    invites_sent = relationship("Invite", foreign_keys="Invite.sender_id", back_populates="sender", cascade="all, delete-orphan")
    editor_projects = relationship("Editor", back_populates="user", cascade="all, delete-orphan")
    prompts = relationship("Prompt", back_populates="user", cascade="all, delete-orphan")
    dm_threads_one = relationship("DmThread", foreign_keys="DmThread.user_one_id", cascade="all, delete-orphan")
    dm_threads_two = relationship("DmThread", foreign_keys="DmThread.user_two_id", cascade="all, delete-orphan")
