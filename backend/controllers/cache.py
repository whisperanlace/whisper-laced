from fastapi import APIRouter
# cache.py
router = APIRouter()
@router.get("/cache/clear")
def clear_cache(): pass
