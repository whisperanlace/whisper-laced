# jobs/report_generation_job.py
import logging
from utils.report_utils import generate_user_reports

logger = logging.getLogger(__name__)

def generate_reports():
    try:
        generate_user_reports()
        logger.info("Report generation completed successfully.")
    except Exception as e:
        logger.error(f"Error generating reports: {str(e)}")
