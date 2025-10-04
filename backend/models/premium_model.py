from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from .base import Base

class PremiumModel(Base):
    __tablename__ = "premium_models"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    description = Column(String, nullable=True)
    tier_id = Column(Integer, ForeignKey("tiers.id"))
    is_active = Column(Boolean, default=True)

    tier = relationship("Tier", backref="premium_models")


