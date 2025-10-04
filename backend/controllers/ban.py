from fastapi import APIRouter, Depends, HTTPException, status
# ban.py
router = APIRouter()
@router.post("/ban") 
def ban_user(): pass
