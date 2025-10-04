from pydantic import BaseModel

class FeatureToggleBase(BaseModel):
    feature_name: str
    enabled: bool = False

class FeatureToggleCreate(FeatureToggleBase):
    pass

class FeatureToggleResponse(FeatureToggleBase):
    id: int
    class Config:
        from_attributes = True
