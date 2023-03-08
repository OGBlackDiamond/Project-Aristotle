import os
import requests
import openai

openai.api_key = "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"

def getChat(input) :
    response = openai.Completion.create(
        model="text-davinci-003", 
        prompt=input, 
        temperature=0.5, 
        max_tokens=250
    )

    return response.choices[0].text

def getChatBetter(input) :
    url = "https://api.openai.com/v1/completions"


    payload = {
        "model": "text-davinci-003",
        "prompt": input,
        "max_tokens": 250,
        "temperature": 0.5
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer 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",

    }

    response = requests.post(url, json=payload, headers=headers)

    return response.content.index(0)


# curl https://api.openai.com/v1/completions \
#   -H 'Content-Type: application/json' \
#   -H 'Authorization: Bearer YOUR_API_KEY' \
#   -d '{
#   "model": "text-davinci-003",
#   "prompt": "Say this is a test",
#   "max_tokens": 7,
#   "temperature": 0
# }'
