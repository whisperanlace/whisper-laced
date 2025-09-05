# schemas/feature_schema.py

from pydantic import BaseModel


class FeatureCreate(BaseModel):
    name: str
    description: str
    enabled: bool = True


class FeatureOut(BaseModel):
    id: int
    name: str
    description: str
    enabled: bool

    class Config:
        orm_mode = True
