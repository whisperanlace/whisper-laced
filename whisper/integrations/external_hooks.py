# integrations/external_hooks.py
import aiohttp
import asyncio

async def call_webhook(url: str, payload: dict):
    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=payload) as resp:
            return await resp.json()
