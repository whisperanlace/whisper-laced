# app/Event_hooks.py
from fastapi import FastAPI
from .logger import init_logger
from .scheduler import scheduler
from .tasks import register_background_tasks

logger = init_logger()

def register_startup_shutdown(app: FastAPI):
    @app.on_event("startup")
    async def startup_event():
        logger.info("Starting Whisper-Laced API...")
        # Start scheduler
        scheduler.start()
        # Initialize background tasks if needed
        register_background_tasks(app)
        logger.info("Startup tasks completed.")

    @app.on_event("shutdown")
    async def shutdown_event():
        logger.info("Shutting down Whisper-Laced API...")
        scheduler.shutdown(wait=False)
        logger.info("Shutdown tasks completed.")
