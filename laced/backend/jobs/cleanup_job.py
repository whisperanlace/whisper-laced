# jobs/cleanup_job.py
import logging
from utils.file_utils import delete_temp_files, delete_old_logs

logger = logging.getLogger(__name__)

def cleanup_files():
    try:
        delete_temp_files()
        delete_old_logs()
        logger.info("Cleanup job completed successfully.")
    except Exception as e:
        logger.error(f"Error during cleanup: {str(e)}")
