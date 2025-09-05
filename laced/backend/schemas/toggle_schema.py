# schemas/toggle_schema.py

from pydantic import BaseModel


class ToggleUpdate(BaseModel):
    feature_name: str
    enabled: bool


class ToggleOut(BaseModel):
    feature_name: str
    enabled: bool
