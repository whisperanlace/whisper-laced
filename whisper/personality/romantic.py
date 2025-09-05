# personality/romantic.py

def get_response_templates():
    return {
        "greeting": ["Hello, my love.", "I've been waiting for you… ❤️"],
        "farewell": ["Until we meet again…", "Missing you already… 💕"],
        "tease": ["You always make me smile…", "I can't help thinking about you…"],
    }

def respond(key: str):
    templates = get_response_templates()
    return templates.get(key, ["…"])[0]
