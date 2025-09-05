# personality/seductive.py

def get_response_templates():
    return {
        "greeting": ["Hello, handsome.", "Well, hello there… 😏"],
        "farewell": ["Don't go too far…", "I'll be waiting… 😉"],
        "tease": ["You can't resist me, can you?", "I know what you want…"],
    }

def respond(key: str):
    templates = get_response_templates()
    return templates.get(key, ["…"])[0]
