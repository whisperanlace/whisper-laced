# conversation/response_engine.py
from personality import base_persona

def generate_response(message: str, context: dict, persona_module=base_persona):
    """
    Generates a response based on user message, context, and selected persona.
    Currently uses persona templates and simple echo logic.
    """
    # Could be replaced with AI model call in future
    template_keys = ["greeting", "farewell", "tease"]
    for key in template_keys:
        if key in message.lower():
            return persona_module.respond(key)

    # Default fallback response
    return f"{persona_module.respond('greeting')} You said: {message}"
