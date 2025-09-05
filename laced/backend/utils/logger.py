# utils/logger.py
import logging
import logging.handlers
import json
from typing import Optional

LOG_FORMAT_JSON = True

class JSONFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord) -> str:
        payload = {
            "name": record.name,
            "level": record.levelname,
            "timestamp": self.formatTime(record, self.datefmt),
            "message": record.getMessage(),
            "module": record.module,
            "funcName": record.funcName,
            "lineno": record.lineno,
        }
        if record.exc_info:
            payload["exc_info"] = self.formatException(record.exc_info)
        return json.dumps(payload)

def _build_logger(name: str, level: int = logging.INFO, stream: Optional[bool] = True) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(level)
    if not logger.handlers:
        if stream:
            handler = logging.StreamHandler()
        else:
            handler = logging.handlers.RotatingFileHandler(f"/var/log/{name}.log", maxBytes=10_000_000, backupCount=5)
        formatter = JSONFormatter() if LOG_FORMAT_JSON else logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.propagate = False
    return logger

def get_logger(name: str = "app", level: int = logging.INFO) -> logging.Logger:
    """
    Returns a configured logger. Use this across the codebase for consistent logs.
    """
    return _build_logger(name, level)
