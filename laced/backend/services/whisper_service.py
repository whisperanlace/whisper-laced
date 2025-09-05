import logging
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.whisper_model import WhisperSession
from app.schemas.whisper_schema import WhisperSessionCreate
from app.utils.response_formatter import format_response
from app.utils.lora_utils import generate_image_from_prompt

logger = logging.getLogger(__name__)

class WhisperService:
    @staticmethod
    async def create_session(db: AsyncSession, session_data: WhisperSessionCreate):
        try:
            session = WhisperSession(
                user_id=session_data.user_id,
                session_name=session_data.session_name,
                prompts=[p.dict() for p in session_data.prompts]
            )
            db.add(session)
            await db.commit()
            await db.refresh(session)
            logger.info(f"Whisper session created: {session.id}")
            return session
        except Exception as e:
            logger.error(f"Error creating Whisper session: {e}")
            raise

    @staticmethod
    async def add_prompt(db: AsyncSession, session_id: int, prompt_text: str, metadata: dict = {}):
        try:
            session = await db.get(WhisperSession, session_id)
            if not session:
                raise ValueError("Whisper session not found")
            session.prompts.append({"prompt_text": prompt_text, "metadata": metadata})
            session.updated_at = datetime.utcnow()
            await db.commit()
            await db.refresh(session)
            # Generate image using Laced
            await generate_image_from_prompt(prompt_text, metadata)
            return session
        except Exception as e:
            logger.error(f"Error adding prompt to Whisper session {session_id}: {e}")
            raise
