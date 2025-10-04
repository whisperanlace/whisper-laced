from fastapi import APIRouter
# collection.py
router = APIRouter()
@router.get("/collections")
def list_collections(): pass
