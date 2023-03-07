import requests
import json
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
    snd_file = rf'C:\Users\caden\Documents\Project-Aristotle\speech.mpeg'
    with open("sound_list.json", "r") as f:
        data = json.load(f)
    voice_found = False
    for i in data:
        if i == speech:
            voice_found = True
            break
    if voice_found == False:
        response = requests.post(url, json=payload, headers=headers)
        with open(snd_file, "wb") as f:
            f.write(response.content)
        print(data)
        data.append(speech)
        print(data)

    playsound(snd_file)
    with open("sound_list.json", "w") as write_file:
        json.dump(data, write_file)

speak("deez big nuts")