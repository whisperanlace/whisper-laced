# personality/emotions.py

# Define supported emotional states
EMOTIONS = {
    "neutral": {"prefix": "", "suffix": ""},
    "happy": {"prefix": "😊 ", "suffix": " 😄"},
    "sad": {"prefix": "😔 ", "suffix": " 💔"},
    "angry": {"prefix": "😠 ", "suffix": " 🔥"},
    "flirty": {"prefix": "😏 ", "suffix": " 😉"},
}

def apply_emotion(text: str, emotion: str):
    e = EMOTIONS.get(emotion, EMOTIONS["neutral"])
    return f"{e['prefix']}{text}{e['suffix']}"
