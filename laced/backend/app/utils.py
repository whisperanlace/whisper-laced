# app/utils.py
import uuid
from datetime import datetime
import re

def generate_uuid() -> str:
    return str(uuid.uuid4())

def current_timestamp() -> datetime:
    return datetime.utcnow()

def sanitize_prompt(prompt: str) -> str:
    prompt = prompt.strip()
    prompt = re.sub(r"\s+", " ", prompt)
    return prompt
