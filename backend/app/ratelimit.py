import os, time, threading
from typing import Optional
from fastapi import Request, HTTPException

try:
    import redis  # type: ignore
except Exception:
    redis = None

class RateLimiter:
    def __init__(self, per_minute:int=120):
        self.per_minute = per_minute
        self.redis_url = os.getenv("REDIS_URL") or os.getenv("CELERY_BROKER_URL")
        self.r = None
        if self.redis_url and redis:
            try:
                self.r = redis.from_url(self.redis_url)
                self.r.ping()
            except Exception:
                self.r = None
        if not self.r:
            self._lock = threading.Lock()
            self._bucket = {}

    def check(self, key:str):
        now = int(time.time() // 60)
        if self.r:
            k = f"rl:{key}:{now}"
            c = self.r.incr(k)
            if c == 1:
                self.r.expire(k, 90)
            if c > self.per_minute:
                raise HTTPException(status_code=429, detail="Rate limit exceeded")
        else:
            with self._lock:
                ckey = (key, now)
                self._bucket[ckey] = self._bucket.get(ckey, 0) + 1
                if self._bucket[ckey] > self.per_minute:
                    raise HTTPException(status_code=429, detail="Rate limit exceeded")

limiter = RateLimiter(per_minute=int(os.getenv("RATE_LIMIT_PER_MIN", "120")))
async def limit_dep(request: Request):
    ip = request.client.host if request.client else "unknown"
    ua = request.headers.get("user-agent","")
    key = f"{ip}:{ua[:20]}"
    limiter.check(key)
