# -*- coding: utf-8 -*-
"""
Template Helpers
Prepare backend data for frontend rendering.
Includes formatting, sorting, pagination, and enrichment.
"""

from typing import List, Dict, Any

def format_image_data(images: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Standardize image data for frontend.
    - Ensures consistent keys
    - Adds derived URLs or metadata if needed
    """
    formatted = []
    for img in images:
        formatted.append({
            "id": img.get("id"),
            "url": img.get("url"),
            "name": img.get("name", ""),
            "size": img.get("size", None),
            "uploaded_at": img.get("uploaded_at"),
            "metadata": img.get("metadata", {}),
        })
    return formatted

def paginate(items: List[Any], page: int = 1, page_size: int = 20) -> Dict[str, Any]:
    """
    Return paginated result for frontend.
    """
    total = len(items)
    start = (page - 1) * page_size
    end = start + page_size
    return {
        "items": items[start:end],
        "total": total,
        "page": page,
        "page_size": page_size,
        "pages": (total + page_size - 1) // page_size
    }

def enrich_user_data(users: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Add computed fields to user objects for frontend display.
    """
    enriched = []
    for user in users:
        enriched.append({
            "id": user.get("id"),
            "email": user.get("email"),
            "is_active": user.get("is_active", True),
            "display_name": user.get("name") or user.get("email").split("@")[0],
        })
    return enriched
