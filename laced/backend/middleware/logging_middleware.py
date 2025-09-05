# middleware/Logging_middleware.py

import logging
from fastapi import Request
from datetime import datetime

logger = logging.getLogger("app_logger")
logger.setLevel(logging.INFO)

async def logging_middleware(request: Request, call_next):
    start_time = datetime.utcnow()
    response = await call_next(request)
    process_time = (datetime.utcnow() - start_time).total_seconds()
    logger.info(f"{request.method} {request.url} completed in {process_time}s")
    return response
