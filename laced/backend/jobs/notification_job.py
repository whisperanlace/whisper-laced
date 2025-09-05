# jobs/notification_job.py
import logging
from utils.notification_utils import send_push_notifications

logger = logging.getLogger(__name__)

def dispatch_notifications():
    try:
        send_push_notifications()
        logger.info("Notification job completed successfully.")
    except Exception as e:
        logger.error(f"Error sending notifications: {str(e)}")
