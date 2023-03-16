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

    def getChatBabbage(self, input) :
        url = "https://api.openai.com/v1/completions"


        payload = {
            "model": "text-curie-001",
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
    
    def getChatTurbo(self, input):
        url = "https://api.openai.com/v1/chat/completions"

        payload = {
            "model": "gpt-3.5-turbo",
            "messages": [{"role": "user", "content": f"{input}"}],
            "max_tokens": 250,
            "temperature": 0.7
        }
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.key}",

        }

        response = requests.post(url, json=payload, headers=headers)

        return response.json()["choices"][0]["message"]["content"]
