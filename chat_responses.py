import os
import requests
import openai

# get the API key from the system variable 
openai.api_key = os.environ["OPENAI_API_KEY"]

"""
This class will allow us to get text responses from ChatGPT
This allows us to simulate a personality when used with
the directive
"""
class Chat:
    # pass in the API key
    def __init__(self):
        self.key = openai.api_key
        pass

    # old code to get responses, this should only be used for testing
    def get_chat_old(self, input) :
        response = openai.Completion.create(
            model="text-davinci-003", 
            prompt=input, 
            temperature=0.5, 
            max_tokens=250
        )

        return response.choices[0].text

    """
    gets a response from the curie voice model
    the curie voice model is faster than turbo,
    but the responses tend to be shorter,
    and less complex
    """
    def get_chat_curie(self, input) :
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

    """
    gets a response from the turbo voice model
    the turbo voice model is slower than curie,
    but the responses tend to be longer,
    and more complex
    """
    def get_chat_turbo(self, input):
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
