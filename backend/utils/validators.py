from typing import Optional

def non_empty_str(v: Optional[str]) -> str:
    if not v or not v.strip():
        raise ValueError("must be non-empty")
    return v.strip()
