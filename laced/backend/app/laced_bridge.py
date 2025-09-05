# app/Laced_bridge.py
from fastapi import FastAPI
from .services import Generation_service, Lora_service
from .Prompt_cleaner import clean_prompt
from .logger import init_logger

logger = init_logger()

def register_laced_endpoints(app: FastAPI):
    gen_service = Generation_service.GenerationService()
    lora_service = Lora_service.LoRAService()

    @app.post("/generate")
    async def generate(content: dict):
        """
        Unified endpoint for image/video/avatar generation.
        Expects: {"prompt": "...", "type": "image/video/avatar", "lora_id": optional}
        """
        prompt = clean_prompt(content.get("prompt", ""))
        content_type = content.get("type", "image")
        lora_id = content.get("lora_id")

        if content_type == "image":
            return await gen_service.generate_image(prompt, lora_id)
        elif content_type == "video":
            return await gen_service.generate_video(prompt, lora_id)
        elif content_type == "avatar":
            return await gen_service.generate_avatar(prompt, lora_id)
        else:
            return {"error": "Invalid generation type"}
