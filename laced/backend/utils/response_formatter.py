# utils/response_formatter.py
from typing import Any, Dict, Optional

def format_success(data: Any = None, message: str = "Success", meta: Optional[Dict] = None) -> Dict[str, Any]:
    resp = {"status": "success", "message": message}
    if data is not None:
        resp["data"] = data
    if meta is not None:
        resp["meta"] = meta
    return resp

def format_error(message: str = "Error", code: int = 400, details: Optional[Any] = None) -> Dict[str, Any]:
    resp = {"status": "error", "message": message, "code": code}
    if details is not None:
        resp["details"] = details
    return resp
