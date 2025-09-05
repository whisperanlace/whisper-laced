# jobs/image_processing_job.py
import asyncio
import logging
from utils.image_utils import resize_image, apply_watermark
from utils.file_utils import get_pending_images

logger = logging.getLogger(__name__)

async def process_images():
    try:
        pending_images = get_pending_images()
        for image_path in pending_images:
            resized = resize_image(image_path)
            apply_watermark(resized)
            logger.info(f"Processed image: {image_path}")
    except Exception as e:
        logger.error(f"Error processing images: {str(e)}")
        # Optional: implement retry logic here
