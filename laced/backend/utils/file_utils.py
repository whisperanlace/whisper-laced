# utils/file_utils.py
import os
from pathlib import Path
from typing import List, Optional
import shutil
import zipfile
import logging
import uuid

logger = logging.getLogger(__name__)

BASE_MEDIA_DIR = Path(os.getenv("MEDIA_ROOT", "/var/app/media"))
TEMP_DIR = BASE_MEDIA_DIR / "temp"
IMAGES_DIR = BASE_MEDIA_DIR / "images"
LORAS_DIR = BASE_MEDIA_DIR / "loras"

# Ensure directories exist at import time (idempotent)
for d in (BASE_MEDIA_DIR, TEMP_DIR, IMAGES_DIR, LORAS_DIR):
    try:
        d.mkdir(parents=True, exist_ok=True)
    except Exception:
        logger.exception(f"Failed creating directory {d}")

def save_file_stream(stream, dest: Path, chunk_size: int = 1024 * 64) -> Path:
    """
    Save binary stream (file-like) to destination path. Returns saved path.
    """
    dest = Path(dest)
    dest.parent.mkdir(parents=True, exist_ok=True)
    with open(dest, "wb") as f:
        while True:
            chunk = stream.read(chunk_size)
            if not chunk:
                break
            f.write(chunk)
    logger.info(f"Saved file to {dest}")
    return dest

def create_temp_file_name(prefix: str = "tmp", ext: str = "") -> Path:
    filename = f"{prefix}_{uuid.uuid4().hex}{ext}"
    return TEMP_DIR / filename

def list_files(directory: Path, pattern: str = "*") -> List[Path]:
    return [p for p in directory.glob(pattern) if p.is_file()]

def delete_temp_files(older_than_seconds: int = 60 * 60 * 24) -> int:
    """
    Delete files from TEMP_DIR older than older_than_seconds. Returns number deleted.
    """
    import time
    now = time.time()
    count = 0
    for p in list_files(TEMP_DIR):
        try:
            if now - p.stat().st_mtime > older_than_seconds:
                p.unlink()
                count += 1
                logger.debug(f"Deleted temp file: {p}")
        except Exception:
            logger.exception(f"Failed deleting temp file {p}")
    return count

def zip_paths(paths: List[Path], output_path: Path) -> Path:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output_path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for p in paths:
            zf.write(p, arcname=p.name)
    logger.info(f"Created zip archive {output_path} containing {len(paths)} files")
    return output_path

def get_pending_images() -> List[Path]:
    """
    Example helper used by jobs.image_processing_job to fetch images flagged for processing.
    Production should adapt to however pending images are tracked (DB or queue).
    Here: return all files in IMAGES_DIR/pending
    """
    pending_dir = IMAGES_DIR / "pending"
    pending_dir.mkdir(parents=True, exist_ok=True)
    return list_files(pending_dir)
