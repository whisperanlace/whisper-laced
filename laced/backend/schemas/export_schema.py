# schemas/export_schema.py

from pydantic import BaseModel


class ExportOut(BaseModel):
    resource_type: str
    url: str
