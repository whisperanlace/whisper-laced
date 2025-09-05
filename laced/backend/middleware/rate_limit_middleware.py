# middleware/Rate_limit_middleware.py

from fastapi import Request, HTTPException
from starlette.responses import Response
from collections import defaultdict
import time

REQUEST_COUNTS = defaultdict(list)
MAX_REQUESTS = 100
WINDOW_SECONDS = 60

async def rate_limit_middleware(request: Request, call_next):
    user_ip = request.client.host
    now = time.time()
    REQUEST_COUNTS[user_ip] = [t for t in REQUEST_COUNTS[user_ip] if t > now - WINDOW_SECONDS]
    if len(REQUEST_COUNTS[user_ip]) >= MAX_REQUESTS:
        raise HTTPException(status_code=429, detail="Too Many Requests")
    REQUEST_COUNTS[user_ip].append(now)
    response = await call_next(request)
    return response
