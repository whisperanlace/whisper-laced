from fastapi import Request, HTTPException
import logging

logger = logging.getLogger(__name__)

class WhisperRateLimitMiddleware:
    def __init__(self, app, max_requests_per_minute: int = 30):
        self.app = app
        self.max_requests = max_requests_per_minute
        self.user_requests = {}

    async def __call__(self, request: Request, call_next):
        user_id = request.headers.get("X-User-ID")
        if not user_id:
            raise HTTPException(status_code=400, detail="User ID missing")

        count = self.user_requests.get(user_id, 0)
        if count >= self.max_requests:
            logger.warning(f"User {user_id} rate limit exceeded")
            raise HTTPException(status_code=429, detail="Rate limit exceeded")
        self.user_requests[user_id] = count + 1

        response = await call_next(request)
        return response
