import os, time, uuid, logging, json
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse, Response
from starlette.middleware.base import BaseHTTPMiddleware

from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded

import sentry_sdk
from sentry_sdk.integrations.starlette import StarletteIntegration

from backend.config.prod_settings import settings
from backend.app.cors import get_cors_config
from backend.routes.metrics_routes import router as metrics_router
try:
    from backend.routes.auth_routes import router as auth_router
    from backend.routes.users_routes import router as users_router
except Exception:
    auth_router = None
    users_router = None

# --- Sentry (no-op if DSN not set) ---
if settings.SENTRY_DSN:
    sentry_sdk.init(dsn=settings.SENTRY_DSN, integrations=[StarletteIntegration()], traces_sample_rate=0.0)

# --- JSON logging ---
class JsonFormatter(logging.Formatter):
    def format(self, record):
        payload = {
            "ts": int(time.time() * 1000),
            "level": record.levelname,
            "logger": record.name,
            "msg": record.getMessage(),
        }
        if record.exc_info:
            payload["exc_info"] = self.formatException(record.exc_info)
        return json.dumps(payload)

h = logging.StreamHandler()
h.setFormatter(JsonFormatter())
root = logging.getLogger()
root.handlers = [h]
root.setLevel(logging.INFO)
logger = logging.getLogger("whisper-laced")

# --- Rate limiting ---
limiter = Limiter(key_func=get_remote_address, default_limits=["60/minute"])

class SecurityHeadersMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        req_id = request.headers.get("X-Request-ID") or uuid.uuid4().hex
        start = time.time()
        try:
            response: Response = await call_next(request)
        except Exception:
            logger.exception("Unhandled error")
            response = JSONResponse({"detail": "Server error"}, status_code=500)
        dur_ms = int((time.time() - start) * 1000)
        response.headers["X-Request-ID"] = req_id
        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["X-Frame-Options"] = "DENY"
        response.headers["Referrer-Policy"] = "no-referrer"
        response.headers["Cache-Control"] = "no-store"
        response.headers["Content-Security-Policy"] = "default-src 'none'; frame-ancestors 'none';"
        logger.info(json.dumps({
            "event": "http_access",
            "req_id": req_id,
            "method": request.method,
            "path": request.url.path,
            "status": response.status_code,
            "dur_ms": dur_ms
        }))
        return response

openapi_on = settings.OPENAPI_ENABLED
app = FastAPI(docs_url=None, redoc_url=None, openapi_url="/openapi.json" if openapi_on else None)

# SlowAPI hookup: MUST register handler by exception class, not an attribute
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

# CORS + security headers
cors = get_cors_config()
app.add_middleware(
    CORSMiddleware,
    allow_origins=cors["allow_origins"],
    allow_credentials=cors["allow_credentials"],
    allow_methods=cors["allow_methods"],
    allow_headers=cors["allow_headers"],
)
app.add_middleware(SecurityHeadersMiddleware)

# Routers
app.include_router(metrics_router)
if auth_router:
    app.include_router(auth_router)
if users_router:
    app.include_router(users_router)

@app.get("/")
@limiter.limit("120/minute")
async def root(request: Request):
    return {"ok": True}

@app.get("/health")
async def health():
    return {"status": "ok"}
