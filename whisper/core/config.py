# core/config.py
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "../.env"))

class Config:
    BOT_TOKEN: str = os.getenv("BOT_TOKEN", "")
    COMMAND_PREFIX: str = os.getenv("COMMAND_PREFIX", "/")
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")
    LACED_API_URL: str = os.getenv("LACED_API_URL", "http://localhost:5000/api")
    LACED_API_KEY: str = os.getenv("LACED_API_KEY", "")
    MAX_PROMPT_BATCH: int = int(os.getenv("MAX_PROMPT_BATCH", 25))
    DEFAULT_PERSONA: str = os.getenv("DEFAULT_PERSONA", "base")
    STORAGE_PATH: str = os.getenv("STORAGE_PATH", "storage/")

config = Config()
