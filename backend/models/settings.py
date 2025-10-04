from sqlalchemy import Column, Integer, ForeignKey, Boolean
from .base import Base
from sqlalchemy.orm import relationship

class UserSettings(Base):
    __tablename__ = "user_settings"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True)
    tier_id = Column(Integer, ForeignKey("tiers.id"))
    notifications_enabled = Column(Boolean, default=True)

    tier = relationship("Tier")


