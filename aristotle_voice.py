import requests
import os
from playsound import playsound
class Response:

    def __init__(self):
        self.snd_filename = "speech.mpeg"
        self.apikey0 = "ecc818f995a03efb02c092423f2aff30"
        self.apikey1 = "2f36a943abb7f73415bb07c75afce3fb"
        self.apikey2 = "7c999b0cc57ce872852c5b03a1bc3d8a"
        self.apikey3 = "d2e4763d403a91991eebab6433742972"

        self.api_keys = [self.apikey0, self.apikey1, self.apikey2, self.apikey3]

        self.currentkey = 2

    #Voice model by Evenlabs
    def speak(self, speech):

        # quick fix to make playsound work
        if os.path.exists(self.snd_filename):
            os.remove(self.snd_filename)

        #switches API keys if needed to make sure we have sufficent words
        self.switch_keys()

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
            "xi-api-key": self.api_keys[self.currentkey],
            "Content-Type": "application/json",
        }

        # defines the file path for the soundfile to go
        snd_file = os.path.join(os.path.dirname(__file__), self.snd_filename)
        
        # gets the response from the API
        response = requests.post(url, json=payload, headers=headers)
        
        #writes the data from the file
        with open(snd_file, "wb") as f:
            f.write(response.content)

        #finally, plays the sound
        playsound(snd_file)


    # this function will check to see how many characters are left in the current API key
    def get_remaining_characters(self):
        url = "https://api.elevenlabs.io/v1/user/subscription"

        headers = {
            "accept": "application/json",
            "xi-api-key": self.api_keys[self.currentkey]
        }

        response = requests.get(url, headers=headers)
        remaining_characters = response.json()["character_count"]
        total_characters = response.json()["character_limit"]
        return total_characters - remaining_characters


    # switches which API key will be used, if one gets low
    def switch_keys(self):
        if self.get_remaining_characters() < 100:
            if self.currentkey == len(self.api_keys):
                self.currentkey = 0
            else:
                self.currentkey += 1
