from pydantic import BaseModel

class SystemFlagBase(BaseModel):
    key: str
    value: bool = False

class SystemFlagCreate(SystemFlagBase):
    pass

class SystemFlagResponse(SystemFlagBase):
    id: int
    class Config:
        from_attributes = True
