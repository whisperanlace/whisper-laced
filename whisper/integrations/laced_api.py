# integrations/laced_api.py
from core.bridge import laced_bridge

async def send_to_laced(prompt: str, user_id: str):
    """
    Sends a prompt to Laced and returns the result.
    Wrapper around core.bridge.laced_bridge.
    """
    result = await laced_bridge.send_prompt(prompt, user_id)
    return result
