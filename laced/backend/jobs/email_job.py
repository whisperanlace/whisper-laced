# jobs/email_job.py
import logging
from utils.email_utils import send_email_batch

logger = logging.getLogger(__name__)

def send_emails():
    try:
        send_email_batch()
        logger.info("Email batch job completed successfully.")
    except Exception as e:
        logger.error(f"Error sending emails: {str(e)}")
