from sqlalchemy.orm import Session
from typing import List
from backend.models import WhisperPrompt
from backend.schemas.whisper_model_schema import WhisperPromptCreate


def create_prompt_entry(db: Session, prompt_data: WhisperPromptCreate) -> WhisperPrompt:
    prompt = WhisperPrompt(**prompt_data.dict())
    db.add(prompt)
    db.commit()
    db.refresh(prompt)
    return prompt


def get_prompts_by_user(db: Session, user_id: int) -> List[WhisperPrompt]:
    return db.query(WhisperPrompt).filter(WhisperPrompt.user_id == user_id).order_by(WhisperPrompt.created_at.desc()).all()

