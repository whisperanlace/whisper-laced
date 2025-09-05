# utils/request_validator.py
from typing import Any, Dict, Tuple
from pydantic import BaseModel, ValidationError
import logging

logger = logging.getLogger(__name__)

def validate_with_pydantic(model: BaseModel, payload: Dict[str, Any]) -> Tuple[bool, Any]:
    """
    Validate payload dict against a provided Pydantic model class (not instance).
    Returns (True, parsed_obj) or (False, error_obj)
    """
    try:
        obj = model.parse_obj(payload)
        return True, obj
    except ValidationError as exc:
        logger.debug(f"Validation error: {exc.json()}")
        return False, exc
