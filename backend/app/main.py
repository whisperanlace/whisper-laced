import logging, os, time, uuid
from typing import Callable
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse, Response
from backend.app.cors import get_cors_config
from backend.routes.metrics_routes import router as metrics_router
from backend.routes.auth_routes import router as auth_router
from backend.routes.users_routes import router as users_router

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(name)s %(message)s")
logger = logging.getLogger("whisper-laced")

class SecurityHeadersMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next: Callable):
        req_id = request.headers.get("X-Request-ID") or uuid.uuid4().hex
        start = time.time()
        try:
            response: Response = await call_next(request)
        except Exception:
            logger.exception("Unhandled error")
            response = JSONResponse({"detail":"Server error"}, status_code=500)
        dur_ms = int((time.time()-start)*1000)
        response.headers["X-Request-ID"] = req_id
        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["X-Frame-Options"] = "DENY"
        response.headers["Referrer-Policy"] = "no-referrer"
        response.headers["Cache-Control"] = "no-store"
        response.headers["Content-Security-Policy"] = "default-src 'none'; frame-ancestors 'none';"
        logger.info("req_id=%s %s %s %s %dms", req_id, request.method, request.url.path, response.status_code, dur_ms)
        return response

openapi_on = os.getenv("OPENAPI_ENABLED","1").lower() not in ("0","false","no")
app = FastAPI(docs_url=None, redoc_url=None, openapi_url="/openapi.json" if openapi_on else None)

cors = get_cors_config()
app.add_middleware(CORSMiddleware,
    allow_origins=cors["allow_origins"],
    allow_credentials=cors["allow_credentials"],
    allow_methods=cors["allow_methods"],
    allow_headers=cors["allow_headers"])
app.add_middleware(SecurityHeadersMiddleware)

# Routers
app.include_router(metrics_router)
app.include_router(auth_router)
app.include_router(users_router)

@app.get("/")
async def root():
    return {"ok": True}

@app.get("/health")
async def health():
    return {"status":"ok"}

# ---- injected by setup ----
from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health():
    return {"ok": True}
# ---- end injection ----
