import os
import requests
import openai

"""
This class will allow us to get text responses from ChatGPT
Proper utilization allows us to simulate a personality when used with
the directive
"""
class Chat:
    # pass in the API keys and urls
    def __init__(self, urls, keys, directive):

        # checks if a key is present in the config file
        if keys["openai_key"] != "":
            # attempt to get the OpenAI API key from the system variable
            try:
                self.key = os.environ["OPENAI_API_KEY"]
            except:
                print("Oops! Something went wrong when trying to get the openAI key from your machine!")
                print("Make sure you have a key, and the system variable has the correct name!")
                quit()
        else:
            # uses the openai key in the config file
            self.key = keys["openai_key"]

        # variable to store all the request urls
        self.urls = urls

        # variable to store the directive, this will be passed into the API request
        self.directive = directive

        # contains the messages in the current conversation
        self.messages = []


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
        return self.get_request("text-curie-001", input)


    """
    gets a response from the turbo voice model
    the turbo voice model is slower than curie,
    but the responses tend to be longer,
    and more complex
    """
    def get_chat_turbo(self, input):
        return self.get_request("gpt-3.5-turbo", input)


    # method that handles all requests to the API, including varied chat models
    def get_request(self, chat_model, input):

        self.messages.append(input)

        # keeps track of the 'back and forth' of a conversation
        conversation_control = 0

        # starts a default payload which imposes the directive
        payload_message =[
            {"role": "system", "content": f"{self.directive}"},
        ]

        # loops through the messages in the current conversation and adds them to the payload
        for message in self.messages:
            if conversation_control % 2 == 0:
                payload_message.append({"role": "user", "content": f"{message}"})
            else:
                payload_message.append({"role": "assistant", "content": f"{message}"})

            conversation_control += 1

        # adds the new input to the payload
        payload_message.append({"role": "user", "content": f"{input}"})

        # the response from the API in text form
        text_response = ""

        # determines which model to request data from
        if chat_model == "gpt-3.5-turbo":
            url = self.urls["chat_completions_url"]
        elif chat_model == "text-curie-001":
            url = self.urls["completions_url"]
        else:
            url = ""

        # compiles the payload
        payload = {
            "model": chat_model,
            "messages": payload_message,
            "max_tokens": 250,
            "temperature": 0.5,
        }
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.key}",

        }

        # makes the request
        response = requests.post(url, json=payload, headers=headers)

        # interprets the response
        if chat_model == "gpt-3.5-turbo":
            text_response = response.json()["choices"][0]["message"]["content"]
        elif chat_model == "text-curie-001":
            text_response = response.json()["choices"][0]["text"]

        # adds the response to the list of messages
        self.messages.append(text_response)

        # returns the text to be spoken
        return text_response


    # clears the current message thread
    def clear_messages(self):
        self.messages = []

    # for later -
    def summarize_conversation(self):
        return self.get_chat_turbo("summarize the conversation we just had")