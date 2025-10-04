from fastapi import APIRouter
from pydantic import BaseModel, Field

router = APIRouter(prefix="/whisper", tags=["whisper"])

class PromptIn(BaseModel):
    prompt: str = Field(..., min_length=1, max_length=4000)

@router.post("/prompt")
def send_prompt(payload: PromptIn):
    # Return a deterministic ack with required "reply" field for tests
    return {
        "status": "accepted",
        "prompt": payload.prompt,
        "reply": f"echo: {payload.prompt}"
    }
