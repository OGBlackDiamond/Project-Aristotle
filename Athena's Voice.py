import requests

from playsound import playsound

url = "https://api.uberduck.ai/speak-synchronous"

payload = {
    "voice": "lj",
    "pace": 1,
    "duration": [1],
    "pitch": [1],
    "voicemodel_uuid": "d927745c-9cff-45e6-bd21-e605c3fa6f5a",
    "speech": "BAZINGA!"
}
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": "Basic cHViX21wbGprYnB5cmdudXZoaGJkeDpwa182ZWMyOTM3Mi1mMTBjLTQzZTItOGZhNi1lNDRjZmE4ZjZkNTg="
}


response = requests.post(url, json=payload, headers=headers)
with open("bazinga.wav", "wb") as f:
    f.write(response.content)

playsound("bazinga.wav")