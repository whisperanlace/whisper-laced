# integrations/storage.py
import os
import json
from core.config import config

def save_user_history(user_id: str, history: dict):
    os.makedirs(config.STORAGE_PATH, exist_ok=True)
    path = os.path.join(config.STORAGE_PATH, f"{user_id}.json")
    with open(path, "w") as f:
        json.dump(history, f)

def load_user_history(user_id: str):
    path = os.path.join(config.STORAGE_PATH, f"{user_id}.json")
    if os.path.exists(path):
        with open(path, "r") as f:
            return json.load(f)
    return {"history": []}
