# schemas/settings_schema.py

from pydantic import BaseModel


class SettingsUpdate(BaseModel):
    key: str
    value: str


class SettingsOut(BaseModel):
    key: str
    value: str
