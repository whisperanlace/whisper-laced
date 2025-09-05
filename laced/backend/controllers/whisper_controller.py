from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.services.whisper_service import WhisperService
from app.schemas.whisper_schema import WhisperSessionCreate, WhisperSessionResponse
from app.dependencies import get_db

router = APIRouter(prefix="/whisper", tags=["Whisper"])

@router.post("/sessions", response_model=WhisperSessionResponse)
async def create_whisper_session(session_data: WhisperSessionCreate, db: AsyncSession = Depends(get_db)):
    try:
        session = await WhisperService.create_session(db, session_data)
        return session
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/sessions/{session_id}/prompts", response_model=WhisperSessionResponse)
async def add_prompt(session_id: int, prompt_text: str, db: AsyncSession = Depends(get_db)):
    try:
        session = await WhisperService.add_prompt(db, session_id, prompt_text)
        return session
    except ValueError as ve:
        raise HTTPException(status_code=404, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
