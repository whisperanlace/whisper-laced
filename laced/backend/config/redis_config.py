# -*- coding: utf-8 -*-
"""
Redis client configuration for Laced.
Provides connection pool and health check.
"""

import redis
from .settings import settings

redis_client = redis.Redis.from_url(settings.REDIS_URL, decode_responses=True)

def check_redis_connection() -> bool:
    try:
        return redis_client.ping()
    except redis.ConnectionError:
        return False
