# schemas/cache_schema.py

from pydantic import BaseModel


class CacheOut(BaseModel):
    cleared: bool
