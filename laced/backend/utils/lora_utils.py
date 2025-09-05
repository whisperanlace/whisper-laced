# utils/lora_utils.py
from typing import Any, Dict, Optional
from pathlib import Path
import logging
from utils.file_utils import LORAS_DIR

logger = logging.getLogger(__name__)

def save_lora_model(model_bytes: bytes, name: str) -> Path:
    """
    Save LoRA model bytes to disk. Returns path.
    """
    LORAS_DIR.mkdir(parents=True, exist_ok=True)
    path = LORAS_DIR / f"{name}.pt"
    with open(path, "wb") as f:
        f.write(model_bytes)
    logger.info(f"Saved LoRA model to {path}")
    return path

def load_lora_model(name: str) -> bytes:
    path = LORAS_DIR / f"{name}.pt"
    if not path.exists():
        logger.error(f"LoRA model not found: {path}")
        raise FileNotFoundError(f"LoRA model not found: {name}")
    with open(path, "rb") as f:
        data = f.read()
    logger.info(f"Loaded LoRA model {name}")
    return data

def load_dataset(dataset_path: Optional[Path] = None) -> Dict[str, Any]:
    """
    Placeholder for dataset loading logic used by training jobs.
    Should return a structure acceptable by training pipeline.
    This implementation expects dataset_path to be a folder with images/annotations.
    """
    if dataset_path is None:
        dataset_path = Path("/var/app/datasets/default")
    if not dataset_path.exists():
        logger.error(f"Dataset path does not exist: {dataset_path}")
        raise FileNotFoundError(f"Dataset not found: {dataset_path}")
    # Minimal representation
    return {"path": str(dataset_path), "num_samples": len(list(dataset_path.glob('**/*.*')))}
