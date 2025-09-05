# personality/playful.py

def get_response_templates():
    return {
        "greeting": ["Hey there, silly!", "Hello, you! 😄"],
        "farewell": ["Bye-bye!", "Catch you later!"],
        "tease": ["Haha, is that all you've got?", "Try harder! 😜"],
    }

def respond(key: str):
    templates = get_response_templates()
    return templates.get(key, ["…"])[0]
