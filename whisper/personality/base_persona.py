# personality/base_persona.py

def get_response_templates():
    return {
        "greeting": ["Hello there.", "Hi, how can I help you today?"],
        "farewell": ["Goodbye!", "Talk soon!"],
        "tease": ["You think you can keep up?", "Oh really? 😏"],
    }

def respond(key: str):
    templates = get_response_templates()
    return templates.get(key, ["..."])[0]
