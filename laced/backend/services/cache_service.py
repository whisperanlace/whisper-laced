import aioredis
from fastapi import HTTPException

class CacheService:

    def __init__(self, redis_url="redis://localhost:6379"):
        self.redis = aioredis.from_url(redis_url, decode_responses=True)

    async def set(self, key: str, value, expire: int = 3600):
        try:
            await self.redis.set(key, value, ex=expire)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    async def get(self, key: str):
        try:
            return await self.redis.get(key)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    async def delete(self, key: str):
        try:
            return await self.redis.delete(key)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
