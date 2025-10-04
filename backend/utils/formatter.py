def to_snake(s: str) -> str:
    import re
    s = re.sub(r"([A-Z]+)", r"_\1", s).lower()
    return s.strip("_")
