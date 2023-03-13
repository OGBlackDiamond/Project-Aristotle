import os
import requests
import openai

openai.api_key = os.environ["OPENAI_API_KEY"]

class Chat:
    def __init__(self):
        self.key = openai.api_key
        pass
    def getChatOld(self, input) :
        response = openai.Completion.create(
            model="text-davinci-003", 
            prompt=input, 
            temperature=0.5, 
            max_tokens=250
        )

        return response.choices[0].text

    def getChat(self, input) :
        url = "https://api.openai.com/v1/completions"


        payload = {
            "model": "text-davinci-003",
            "prompt": input,
            "max_tokens": 250,
            "temperature": 0.5
        }
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.key}",

        }

        response = requests.post(url, json=payload, headers=headers)

        return response.json()["choices"][0]["text"]