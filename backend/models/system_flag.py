from sqlalchemy import Column, Integer, String, Boolean
from .base import Base

class SystemFlag(Base):
    __tablename__ = "system_flags"

    id = Column(Integer, primary_key=True, index=True)
    key = Column(String, unique=True, index=True, nullable=False)
    value = Column(Boolean, default=False, nullable=False)


