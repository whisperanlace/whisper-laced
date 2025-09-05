# personality/custom.py

# Allows user-defined responses
CUSTOM_TEMPLATES = {}

def set_custom_templates(templates: dict):
    global CUSTOM_TEMPLATES
    CUSTOM_TEMPLATES = templates

def respond(key: str):
    return CUSTOM_TEMPLATES.get(key, ["…"])[0]
