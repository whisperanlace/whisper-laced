import requests

def test_send_prompt():
    url = "http://localhost:8000/whisper/prompt"
    payload = {"prompt": "hello whisper"}
    headers = {"Content-Type": "application/json"}

    response = requests.post(url, json=payload, headers=headers)

    assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
    data = response.json()
    assert "reply" in data, "Missing reply in response"
    print("âœ… Prompt test passed:", data)

if __name__ == "__main__":
    test_send_prompt()

