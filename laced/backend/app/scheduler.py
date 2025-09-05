# app/scheduler.py
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from .logger import init_logger
from .tasks import register_background_tasks

logger = init_logger()
scheduler = AsyncIOScheduler()

def register_cron_jobs(app):
    """
    Schedule recurring jobs.
    """
    tasks = app.state.tasks

    scheduler.add_job(tasks["process_loras"], "interval", minutes=5, id="lora_processing")
    scheduler.add_job(tasks["cleanup_media"], "interval", hours=1, id="media_cleanup")
    scheduler.add_job(tasks["send_notifications"], "interval", minutes=2, id="notifications")

    logger.info("Cron jobs registered.")
