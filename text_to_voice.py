import requests
import os
from dotenv import load_dotenv

load_dotenv()

ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
VOICE_ID = os.getenv("ELEVENLABS_VOICE_ID")  # << You should add this to your .env

def speak(text, filename="ai_voice.mp3"):
    if not ELEVENLABS_API_KEY or not VOICE_ID:
        print("❌ ELEVENLABS_API_KEY or VOICE_ID is missing.")
        return

    url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"
    headers = {
        "xi-api-key": ELEVENLABS_API_KEY,
        "Content-Type": "application/json"
    }
    data = {
        "text": text,
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.75
        }
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        with open(filename, "wb") as f:
            f.write(response.content)
        print(f"🎧 Voice saved to {filename}")
        # Optional: play the file using a system call
        # os.system(f"afplay {filename}")  # macOS only
    else:
        print("❌ Failed to generate voice:", response.text)
