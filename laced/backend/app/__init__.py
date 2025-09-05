# app/__init__.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from starlette.middleware.sessions import SessionMiddleware
from starlette.middleware.trustedhost import TrustedHostMiddleware

from .config import settings
from .database import init_db
from .logger import init_logger
from .utils import current_timestamp

logger = init_logger()

app = FastAPI(
    title="Whisper-Laced API",
    description="Fully integrated AI content generation platform: image, video, avatar, LoRA, editor, community.",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json"
)

# Middleware
app.add_middleware(GZipMiddleware, minimum_size=1000)
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(
    TrustedHostMiddleware,
    allowed_hosts=settings.TRUSTED_HOSTS
)
app.add_middleware(SessionMiddleware, secret_key=settings.SESSION_SECRET)

# Initialize DB
init_db(app)

# Register hooks, tasks, websockets, scheduler, and bridge
from . import Event_hooks, tasks, Websocket_events, scheduler, Laced_bridge

Event_hooks.register_startup_shutdown(app)
tasks.register_background_tasks(app)
scheduler.register_cron_jobs(app)
Laced_bridge.register_laced_endpoints(app)
Websocket_events.register_ws_events(app)
