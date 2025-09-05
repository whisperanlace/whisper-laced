# core/logger.py
import logging
from core.config import config

def setup_logger(name: str = "whisper"):
    logger = logging.getLogger(name)
    logger.setLevel(config.LOG_LEVEL.upper())

    if not logger.handlers:
        # Console handler
        ch = logging.StreamHandler()
        ch.setLevel(config.LOG_LEVEL.upper())

        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        ch.setFormatter(formatter)
        logger.addHandler(ch)

    return logger

logger = setup_logger()
