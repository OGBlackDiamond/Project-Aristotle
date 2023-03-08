from aristotle_voice import *
from voice_recognition import *
from phrases import *
from chat_responses import *
import json
import random
with open("callsign.json", "r") as f:
        callsign = json.load(f)

has_attention = False

directive = f"You are a virtual assistant named {callsign}. Your creator and companion, Caden Feller is speaking, he tells you "

def command_center(input):
    command = input
    if command == "introduce yourself":
        return f"Hello, my name is {callsign}"
    elif command == "change call sign":
        with open("callsign.json", "w") as write_file:
            json.dump(listen()
                      , write_file)
        return responses()
    else:
        #chat gpt goes burrrr
        return getChat(directive + command)


while True:
    input = listen()
    if has_attention == False:
        if input == callsign:
            has_attention = True
            speak(greetings())
        else: 
            continue
    else:
        if input != 'goodbye':
            speak(command_center(input))
        else:
            speak(input)
            break