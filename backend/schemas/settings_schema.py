from pydantic import BaseModel

class UserSettingsResponse(BaseModel):
    id: int
    user_id: int
    tier_id: int
    notifications_enabled: bool

    class Config:
        from_attributes = True
