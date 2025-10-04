import os
from pydantic import BaseModel, field_validator
from typing import Optional

class Settings(BaseModel):
    ENV: str = os.getenv("ENV", "dev")  # dev|staging|prod
    SECRET_KEY: str = os.getenv("SECRET_KEY", "CHANGE_ME_64_CHAR_MIN")
    ALGORITHM: str = os.getenv("JWT_ALG", "HS256")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30"))
    REFRESH_TOKEN_EXPIRE_DAYS: int = int(os.getenv("REFRESH_TOKEN_EXPIRE_DAYS", "30"))
    PASSWORD_MIN_LENGTH: int = int(os.getenv("PASSWORD_MIN_LENGTH", "12"))
    PASSWORD_REQUIRE_UPPER: bool = os.getenv("PASSWORD_REQUIRE_UPPER","1").lower() not in ("0","false","no")
    PASSWORD_REQUIRE_LOWER: bool = os.getenv("PASSWORD_REQUIRE_LOWER","1").lower() not in ("0","false","no")
    PASSWORD_REQUIRE_DIGIT: bool = os.getenv("PASSWORD_REQUIRE_DIGIT","1").lower() not in ("0","false","no")
    PASSWORD_REQUIRE_SYMBOL: bool = os.getenv("PASSWORD_REQUIRE_SYMBOL","1").lower() not in ("0","false","no")

    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///D:/whisper-laced/backend/db.sqlite3")
    TZ: str = os.getenv("TZ", "UTC")
    OPENAPI_ENABLED: bool = os.getenv("OPENAPI_ENABLED","1").lower() not in ("0","false","no")

    # CORS
    ALLOW_LOCAL_CORS: bool = os.getenv("ALLOW_LOCAL_CORS","1").lower() not in ("0","false","no")
    ALLOW_ORIGINS: Optional[str] = os.getenv("ALLOW_ORIGINS")

    # Optional Redis for rate-limit / session-blacklist
    REDIS_URL: Optional[str] = os.getenv("REDIS_URL") or os.getenv("CELERY_BROKER_URL")

    @property
    def cors_origins(self):
        if self.ALLOW_LOCAL_CORS:
            return ["http://localhost:3000","http://127.0.0.1:3000"]
        if self.ALLOW_ORIGINS:
            return [o.strip() for o in self.ALLOW_ORIGINS.split(",") if o.strip()]
        return ["https://app.whisper-laced.com","https://admin.whisper-laced.com"]

settings = Settings()
