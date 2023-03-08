import requests
import os
from playsound import playsound
#Voice model by Evenlabs
def speak(speech):
    url = "https://api.elevenlabs.io/v1/text-to-speech/pNInz6obpgDQGcFmaJgB"


    payload = {
        "text": speech,
        "voice_settings": {
            "stability": 0.75,
            "similarity_boost": 0.5
        }
    }
    headers = {
        "accept": "audio/mpeg",
        "xi-api-key": "ecc818f995a03efb02c092423f2aff30",
        "Content-Type": "application/json",
    }
    snd_file = 'speech.mpeg'
    response = requests.post(url, json=payload, headers=headers)
    with open(snd_file, "wb") as f:
        f.write(response.content)

    playsound(snd_file)