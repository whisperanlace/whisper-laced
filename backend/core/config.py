from __future__ import annotations

from typing import Optional
from pydantic import Field, AliasChoices
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # Load from .env; accept extra keys without blowing up
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    # Accept BOTH UPPERCASE and legacy lowercase env var names
    DATABASE_URL: str = Field(
        default="sqlite:///D:/whisper-laced/backend/db.sqlite3",
        validation_alias=AliasChoices("DATABASE_URL", "database_url"),
    )
    SECRET_KEY: str = Field(
        default="dev-secret-change-me",
        validation_alias=AliasChoices("SECRET_KEY", "jwt_secret"),
    )
    JWT_ALGORITHM: str = Field(
        default="HS256",
        validation_alias=AliasChoices("JWT_ALGORITHM", "jwt_algo"),
    )
    ACCESS_TOKEN_EXPIRE_MINUTES: int = Field(
        default=60,
        validation_alias=AliasChoices("ACCESS_TOKEN_EXPIRE_MINUTES", "access_token_expire_minutes"),
    )
    # Optional helpers (don’t break if present)
    PYTHONPATH: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices("PYTHONPATH", "pythonpath"),
    )
    DEV_NO_AUTH: bool = Field(
        default=False,
        validation_alias=AliasChoices("DEV_NO_AUTH", "dev_no_auth"),
    )

settings = Settings()
