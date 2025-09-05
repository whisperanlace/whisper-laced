# app/tasks.py
from fastapi import FastAPI
from .services import (
    Lora_service, Image_service, Video_service, Notification_service
)
from .logger import init_logger

logger = init_logger()

def register_background_tasks(app: FastAPI):
    """
    Register recurring or async tasks at app startup.
    """
    lora_service = Lora_service.LoRAService()
    image_service = Image_service.ImageService()
    video_service = Video_service.VideoService()
    notification_service = Notification_service.NotificationService()

    async def process_pending_loras():
        await lora_service.process_queue()

    async def cleanup_unused_media():
        await image_service.cleanup_unused()
        await video_service.cleanup_unused()

    async def send_pending_notifications():
        await notification_service.send_pending()

    # Attach to app state for reference
    app.state.tasks = {
        "process_loras": process_pending_loras,
        "cleanup_media": cleanup_unused_media,
        "send_notifications": send_pending_notifications,
    }
