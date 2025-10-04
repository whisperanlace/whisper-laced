from pydantic import BaseModel

class ToggleBase(BaseModel):
    name: str
    enabled: bool = False

class ToggleCreate(ToggleBase):
    pass

class ToggleResponse(ToggleBase):
    id: int
    class Config:
        from_attributes = True
