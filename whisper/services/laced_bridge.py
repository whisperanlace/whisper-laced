import requests


BACKEND_URL = "http://localhost:8000/whisper/prompt"


def send_prompt_to_backend(user_id: int, prompt_text: str, response_text: str = None):
    try:
        payload = {
            "user_id": user_id,
            "prompt_text": prompt_text,
            "response_text": response_text,
        }
        res = requests.post(BACKEND_URL, json=payload)
        res.raise_for_status()
        return res.json()
    except Exception as e:
        print(f"[Whisper ? Laced] Error sending prompt: {e}")
        return None

