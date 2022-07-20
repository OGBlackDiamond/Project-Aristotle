import requests
import json
from playsound import playsound
#Voice model by uberduck.ai
def speak(speech):
    url = "https://api.uberduck.ai/speak-synchronous"


    payload = {
        "voice": "lj",
        "pace": 1,
        "duration": [1],
        "pitch": [1],
        "voicemodel_uuid": "d927745c-9cff-45e6-bd21-e605c3fa6f5a",
        "speech": speech
    }
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": "Basic cHViX21wbGprYnB5cmdudXZoaGJkeDpwa182ZWMyOTM3Mi1mMTBjLTQzZTItOGZhNi1lNDRjZmE4ZjZkNTg="
    }
    snd_file = rf'C:\Users\caden\Documents\Project-Athena\sound_files\{speech}.wav'
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

