import requests
import os
import json
from playsound import playsound

"""
This class will be used to get audio responses as input
This will be used to simulate ChatGPT talking back to you
"""
class Speech:

    def __init__(self, keys, urls):
        # defines the file where the sound will be temporarily stored
        self.snd_filename = "speech.mpeg"

        # defines the dict of keys that will be used
        self.keys = keys["elevenlabs_keys"]

        # initializes the list for the keys to be placed into
        self.api_keys = []

        # checks that the user has at least one API key to utilize
        if len(self.keys) <= 0:
            # adds all the API keys from the dictionary to a list to be used in the program
            for i in range(len(self.keys)):
                self.api_keys.append(self.keys[f"apikey{i}"])
        else:
            # silly user, they have no API keys haha
            print("Shucks! Your config file has no Elevenlabs API keys!")
            print("Make sure you have at least one, and place it in your config.json file.")
            quit()

        # defines the dict of urls that will be used
        self.urls = urls

        # variable to control what key is currently being used
        self.currentkey = 1

        # defines the urls needed for each voice model
        self.aristotle_url = self.urls["aristotle_url"]
        self.athena_url = self.urls["athena_url"]

    #Voice model by Elevenlabs
    def speak(self, speech, gender):

        # quick fix to make playsound work
        if os.path.exists(self.snd_filename):
            os.remove(self.snd_filename)

        #switches API keys if needed to make sure we have sufficent words
        self.switch_keys()

        # chooses the voice depending of the variable passed in
        if gender == "male":
            url = self.aristotle_url
        elif gender == "female":
            url = self.athena_url
        else:
            url = ""

        # makes the API request
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
        url = self.urls["subscription_url"]

        headers = {
            "accept": "application/json",
            "xi-api-key": self.api_keys[self.currentkey]
        }

        response = requests.get(url, headers=headers)
        # gets how many characters are left on the current key
        remaining_characters = response.json()["character_count"]
        # gets the maximum ammount of characters left in the current API key
        total_characters = response.json()["character_limit"]

        # returns the ammount of characters left
        return total_characters - remaining_characters


    # switches which API key will be used, if one gets low
    def switch_keys(self):
        if self.get_remaining_characters() < 250:
            if self.currentkey == len(self.api_keys):
                self.currentkey = 0
            else:
                self.currentkey += 1
