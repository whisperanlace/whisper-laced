# app/Prompt_cleaner.py
import re
from .utils import sanitize_prompt

def clean_prompt(raw_prompt: str) -> str:
    """
    Clean and normalize prompts for AI generation.
    """
    prompt = sanitize_prompt(raw_prompt)
    # Remove disallowed characters
    prompt = re.sub(r"[^a-zA-Z0-9\s.,!?-]", "", prompt)
    return prompt
