import os
import requests
import openai

"""
This class will allow us to get text responses from ChatGPT
This allows us to simulate a personality when used with
the directive
"""
class Chat:
    # pass in the API key
    def __init__(self, urls):
        try:
            # get the API key from the system variable 
            self.key = os.environ["OPENAI_API_KEY"]
        except:
            print("Oops! Something went wrong when trying to get the openAI key from your machine!")
            print("Make sure you have a key, and the system variable has the correct name!")
            quit()

        self.urls = urls

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
        url = self.urls["completions_url"]

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
        url = self.urls["chat_completions_url"]

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