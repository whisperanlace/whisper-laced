from __future__ import annotations
import os, time, hashlib
from typing import Callable, Awaitable
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import JSONResponse
import redis

R = redis.Redis.from_url(os.getenv("RATE_LIMIT_REDIS", os.getenv("CELERY_BROKER_URL", "redis://127.0.0.1:6379/0")))

RATE = int(os.getenv("RATE_LIMIT_PER_MIN", "120"))
BURST = int(os.getenv("RATE_LIMIT_BURST", "20"))
WINDOW = 60

def _key(req: Request) -> str:
    tok = req.headers.get("authorization") or req.client.host if req.client else "unknown"
    tok = tok.strip().lower()
    h = hashlib.sha256(tok.encode()).hexdigest()[:32]
    return f"rl:{h}"

class RateLimitMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next: Callable[[Request], Awaitable]):
        k = _key(request)
        p = R.pipeline()
        p.incr(k, 1)
        p.expire(k, WINDOW)
        count, _ = p.execute()
        # simple leaky bucket: allow RATE + BURST within WINDOW
        if int(count) > RATE + BURST:
            retry = R.ttl(k)
            return JSONResponse({"detail":"rate limit exceeded","retry_in":max(retry,1)}, status_code=429)
        return await call_next(request)