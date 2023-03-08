from aristotle_voice import *
from voice_recognition import *
from phrases import *
from chat_responses import *
import json
import random
with open("callsign.json", "r") as f:
    callsign = json.load(f)
with open("directive.json", "r") as f:
    directive = json.load(f)

has_attention = False


def command_center(input):
    command = input
    if command == "change call sign":
        with open("callsign.json", "w") as write_file:
            json.dump(listen()
                      , write_file)
        return responses()
    elif command == "append to directive":
        speak("Sure thing. What would you like to add to the directive?")
        with open("directive.json", "w") as write_file:
            json.dump(directive + listen()+ ". ", write_file)
    else:
        #chat gpt goes burrrr
        return getChat(f"{directive}Caden tells you {input}, what do you say?")



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