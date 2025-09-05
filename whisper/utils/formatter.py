# utils/formatter.py

def clean_text(text: str) -> str:
    """Remove extra spaces and line breaks."""
    return " ".join(text.strip().split())
