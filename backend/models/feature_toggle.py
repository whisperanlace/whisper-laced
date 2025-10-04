from sqlalchemy import Column, Integer, String, Boolean
from .base import Base

class FeatureToggle(Base):
    __tablename__ = "feature_toggles"

    id = Column(Integer, primary_key=True, index=True)
    feature_name = Column(String, unique=True, index=True, nullable=False)
    enabled = Column(Boolean, default=False, nullable=False)


