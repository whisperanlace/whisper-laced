# utils/pagination.py
from typing import Dict, Any, Iterable, List
import math

def paginate(items: Iterable, page: int = 1, per_page: int = 20) -> Dict[str, Any]:
    """
    Simple pagination utility returning metadata and items slice.
    Items can be list or SQLAlchemy query that supports slicing.
    """
    if page < 1:
        page = 1
    if per_page < 1:
        per_page = 20
    # Convert to list only when necessary; caller should pass sliceable objects
    try:
        total = len(items)  # may raise if items is a generator
        start = (page - 1) * per_page
        end = start + per_page
        data = items[start:end]
    except TypeError:
        # Items is generator or query; materialize per_page+1 items to detect next page
        materialized: List = list(items)
        total = len(materialized)
        start = (page - 1) * per_page
        end = start + per_page
        data = materialized[start:end]
    pages = math.ceil(total / per_page) if per_page else 0
    return {"items": data, "meta": {"page": page, "per_page": per_page, "total": total, "pages": pages}}
