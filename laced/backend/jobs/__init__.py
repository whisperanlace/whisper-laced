"""
jobs package
------------
This package contains all background jobs for the application, including:
- Image processing
- LoRA training
- Cleanup tasks
- Email & notification dispatch
- Scheduled report generation

All jobs are integrated with the global scheduler and follow production standards:
- Logging
- Error handling
- Retry mechanisms (if applicable)
- Async support where needed
"""

from .job_scheduler import JobScheduler
from .image_processing_job import process_images
from .lora_training_job import train_lora
from .cleanup_job import cleanup_files
from .email_job import send_emails
from .notification_job import dispatch_notifications
from .report_generation_job import generate_reports

__all__ = [
    "JobScheduler",
    "process_images",
    "train_lora",
    "cleanup_files",
    "send_emails",
    "dispatch_notifications",
    "generate_reports",
]
