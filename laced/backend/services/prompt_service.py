# services/prompt_service.py

from sqlalchemy.orm import Session
from models.prompt_model import Prompt
from schemas.prompt_schema import PromptCreate, PromptUpdate
from utils.logger import log_event


class PromptService:
    @staticmethod
    def create_prompt(db: Session, user_id: int, prompt: PromptCreate) -> Prompt:
        new_prompt = Prompt(
            user_id=user_id,
            text=prompt.text,
            metadata=prompt.metadata,
            created_at=prompt.created_at or None,
        )
        db.add(new_prompt)
        db.commit()
        db.refresh(new_prompt)
        log_event("prompt_created", {"prompt_id": new_prompt.id, "user_id": user_id})
        return new_prompt

    @staticmethod
    def get_prompt(db: Session, prompt_id: int) -> Prompt | None:
        return db.query(Prompt).filter(Prompt.id == prompt_id).first()

    @staticmethod
    def list_prompts(db: Session, user_id: int) -> list[Prompt]:
        return db.query(Prompt).filter(Prompt.user_id == user_id).all()

    @staticmethod
    def update_prompt(db: Session, prompt_id: int, update: PromptUpdate) -> Prompt | None:
        prompt = db.query(Prompt).filter(Prompt.id == prompt_id).first()
        if not prompt:
            return None
        for key, value in update.dict(exclude_unset=True).items():
            setattr(prompt, key, value)
        db.commit()
        db.refresh(prompt)
        log_event("prompt_updated", {"prompt_id": prompt.id})
        return prompt

    @staticmethod
    def delete_prompt(db: Session, prompt_id: int, user_id: int) -> bool:
        prompt = db.query(Prompt).filter(
            Prompt.id == prompt_id, Prompt.user_id == user_id
        ).first()
        if not prompt:
            return False
        db.delete(prompt)
        db.commit()
        log_event("prompt_deleted", {"prompt_id": prompt_id, "user_id": user_id})
        return True
