# core/bridge.py
import aiohttp
import asyncio
from core.config import config
from core.logger import logger

class LacedBridge:
    def __init__(self):
        self.api_url = config.LACED_API_URL
        self.api_key = config.LACED_API_KEY
        self.session = aiohttp.ClientSession()

    async def send_prompt(self, prompt: str, user_id: str, batch_size: int = None):
        if batch_size is None:
            batch_size = config.MAX_PROMPT_BATCH

        payload = {
            "prompt": prompt,
            "user_id": user_id,
            "batch_size": batch_size
        }

        headers = {"Authorization": f"Bearer {self.api_key}"}

        try:
            async with self.session.post(f"{self.api_url}/generate", json=payload, headers=headers) as resp:
                if resp.status == 200:
                    data = await resp.json()
                    return data
                else:
                    logger.error(f"Laced API returned {resp.status}")
                    return {"error": f"API returned {resp.status}"}
        except Exception as e:
            logger.exception(f"Exception while calling Laced API: {e}")
            return {"error": str(e)}

    async def close(self):
        await self.session.close()

# Singleton instance
laced_bridge = LacedBridge()
