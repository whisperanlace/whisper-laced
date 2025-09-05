# middleware/Cache_middleware.py

from fastapi import Request
from fastapi.responses import JSONResponse
from functools import lru_cache

@lru_cache(maxsize=1024)
def cached_response(key: str):
    return None

async def cache_middleware(request: Request, call_next):
    key = str(request.url)
    cached = cached_response(key)
    if cached:
        return JSONResponse(content=cached)
    response = await call_next(request)
    return response
