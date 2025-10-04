from fastapi import APIRouter
# feature.py
router = APIRouter()
@router.get("/features")
def list_features(): pass
