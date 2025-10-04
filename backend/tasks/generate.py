from __future__ import annotations
from datetime import datetime, timezone
from typing import Any, Dict, Optional
import os, json, time, uuid
from pathlib import Path

from backend.celery_app import app
from backend.config import settings

# Optional HTTP client; only needed if GENERATOR_MODE=http
try:
    import requests  # type: ignore
except Exception:
    requests = None  # we will guard usage

OUTPUT_DIR = Path(settings.OUTPUT_DIR)
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

def _safe_name(s: str) -> str:
    return "".join(c for c in s if c.isalnum() or c in ("-", "_", ".", " ")).strip()

def _write_json(p: Path, payload: Dict[str, Any]) -> None:
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open("w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2, ensure_ascii=False)

def _local_pipeline(prompt: str, *, task_id: str, **kwargs: Any) -> Path:
    """Replace this with your real local generator; returns file path."""
    # Simulate real work — swap for actual generator call
    time.sleep(0.5)
    out = OUTPUT_DIR / f"{task_id}.json"
    _write_json(out, {"task_id": task_id, "prompt": prompt, "note": "replace with real image path"})
    return out

def _http_pipeline(prompt: str, *, task_id: str, **kwargs: Any) -> Path:
    if requests is None:
        raise RuntimeError("requests not installed but GENERATOR_MODE=http")
    url = settings.GENERATOR_HTTP_URL
    payload = {"task_id": task_id, "prompt": prompt, "params": kwargs}
    resp = requests.post(url, json=payload, timeout=settings.GENERATOR_HTTP_TIMEOUT)
    resp.raise_for_status()
    data = resp.json()

    # Expect either an explicit output_path or a downloadable URL
    output_path: Optional[str] = data.get("output_path")
    download_url: Optional[str] = data.get("url")

    if output_path:
        return Path(output_path)

    if download_url:
        # Save downloaded content to OUTPUT_DIR/<task_id>.png
        bin_resp = requests.get(download_url, timeout=settings.GENERATOR_HTTP_TIMEOUT)
        bin_resp.raise_for_status()
        ext = ".png"
        out = OUTPUT_DIR / f"{task_id}{ext}"
        with out.open("wb") as f:
            f.write(bin_resp.content)
        return out

    # As a last resort, persist whatever data we got
    fallback = OUTPUT_DIR / f"{task_id}.json"
    _write_json(fallback, {"task_id": task_id, "prompt": prompt, "raw": data})
    return fallback

@app.task(name="generate.image", bind=True, autoretry_for=(Exception,), retry_backoff=True, retry_kwargs={"max_retries": 3})
def generate_image_task(self, prompt: str, **kwargs: Any) -> Dict[str, Any]:
    """
    Production-ready wrapper around your generator.
    Switch behavior via GENERATOR_MODE env var: 'http' or 'local'.
    """
    task_id = self.request.id or str(uuid.uuid4())
    started_at = datetime.now(timezone.utc).isoformat()

    mode = settings.GENERATOR_MODE.lower().strip()
    if mode == "http":
        out_path = _http_pipeline(prompt, task_id=task_id, **kwargs)
    elif mode == "local":
        out_path = _local_pipeline(prompt, task_id=task_id, **kwargs)
    else:
        raise RuntimeError(f"Unsupported GENERATOR_MODE={settings.GENERATOR_MODE}")

    result = {
        "task_id": task_id,
        "prompt": prompt,
        "status": "completed",
        "started_at": started_at,
        "completed_at": datetime.now(timezone.utc).isoformat(),
        "output_path": str(out_path),
        "params": kwargs,
        "mode": mode,
    }
    return result

__all__ = ["generate_image_task"]