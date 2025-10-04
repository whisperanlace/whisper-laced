import time
import typing as t
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse
from starlette.types import ASGIApp

# Simple in-memory token bucket per client IP (good enough for single-process dev)
WINDOW = int(float(__import__("os").environ.get("RATE_LIMIT_WINDOW", "60")))
LIMIT  = int(float(__import__("os").environ.get("RATE_LIMIT_LIMIT", "120")))

_buckets: t.Dict[str, t.Tuple[int, int]] = {}
# key -> (tokens, reset_epoch)

class RateLimitMiddleware(BaseHTTPMiddleware):
    def __init__(self, app: ASGIApp):
        super().__init__(app)

    async def dispatch(self, request, call_next):
        ip = (request.client.host if request.client else "unknown")
        now = int(time.time())
        tokens, reset_at = _buckets.get(ip, (LIMIT, now + WINDOW))
        # refill if window reset
        if now >= reset_at:
            tokens, reset_at = (LIMIT, now + WINDOW)
        if tokens <= 0:
            return JSONResponse(
                {"detail": "Rate limit exceeded"},
                status_code=429,
                headers={"X-RateLimit-Reset": str(reset_at)}
            )
        _buckets[ip] = (tokens - 1, reset_at)
        response = await call_next(request)
        response.headers["X-RateLimit-Remaining"] = str(_buckets[ip][0])
        response.headers["X-RateLimit-Reset"] = str(reset_at)
        return response
