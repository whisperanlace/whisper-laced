# jobs/job_scheduler.py
import asyncio
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
import logging
from .image_processing_job import process_images
from .lora_training_job import train_lora
from .cleanup_job import cleanup_files
from .report_generation_job import generate_reports

logger = logging.getLogger(__name__)

class JobScheduler:
    def __init__(self):
        self.scheduler = AsyncIOScheduler()

    def start(self):
        # Schedule jobs
        self.scheduler.add_job(process_images, CronTrigger(hour='*/1'))  # every hour
        self.scheduler.add_job(train_lora, CronTrigger(hour='2'))        # daily at 2am
        self.scheduler.add_job(cleanup_files, CronTrigger(hour='3'))     # daily at 3am
        self.scheduler.add_job(generate_reports, CronTrigger(hour='4'))  # daily at 4am
        logger.info("Scheduler started with all jobs.")
        self.scheduler.start()

# For standalone run
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    scheduler = JobScheduler()
    scheduler.start()
    asyncio.get_event_loop().run_forever()
