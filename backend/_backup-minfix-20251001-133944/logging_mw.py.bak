from __future__ import annotations
import json
import logging
import time
from starlette.middleware.base import BaseHTTPMiddleware

# Dedicated app audit logger (won't use uvicorn.access)
log = logging.getLogger("app.audit")
if not log.handlers:
    h = logging.StreamHandler()
    h.setFormatter(logging.Formatter("%(message)s"))
    log.addHandler(h)
log.propagate = False
log.setLevel(logging.INFO)

class RequestLogMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        t0 = time.perf_counter()
        response = await call_next(request)
        ms = int((time.perf_counter() - t0) * 1000)
        entry = {
            "level": "info",
            "method": request.method,
            "path": request.url.path,
            "status": response.status_code,
            "ms": ms,
            "client": request.client.host if request.client else "-",
        }
        log.info(json.dumps(entry, ensure_ascii=False))
        return response

# Back-compat shim for existing imports in main.py
class AccessLoggingMiddleware(RequestLogMiddleware):
    pass