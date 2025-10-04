import os
from pydantic import BaseModel, ValidationError
class Settings(BaseModel):
    SECRET_KEY: str
    DATABASE_URL: str
    OPENAPI_ENABLED: bool = (os.getenv("OPENAPI_ENABLED","1").lower() not in ("0","false","no"))
    ALLOW_ORIGINS: str = os.getenv("ALLOW_ORIGINS","https://app.whisper-laced.com,https://admin.whisper-laced.com")
    TZ: str = os.getenv("TZ","UTC")
    SENTRY_DSN: str | None = os.getenv("SENTRY_DSN")
try:
    settings = Settings(
        SECRET_KEY=os.getenv("SECRET_KEY"),
        DATABASE_URL=os.getenv("DATABASE_URL"),
    )
except ValidationError as e:
    # Fail hard on boot in prod if required envs missing
    raise SystemExit(f"[CONFIG] Missing/invalid required settings: {e}")
