from aristotle_voice import *
from voice_recognition import *
from phrases import *
import random
with open("callsign.json", "r") as f:
        callsign = json.load(f)

has_attention = False

def command_center(input):
    command = input
    if command == "repeat after me":
        words = ""
        while words != "stop":
            speak(words)
            words = listen()
    elif command == "introduce yourself":
        speak("hello")
        speak(f"my name is {callsign}")
    elif command == "tell me a joke":
        num = int(random.random()*10)
        while num > 4:
            num = int(random.random()*10)
        speak(jokes(num))
        speak(punchlines(num))
    elif command == "change call sign":
        speak(responses())
        speak("what would you like my new call sign to be")
        with open("callsign.json", "w") as write_file:
            json.dump(listen()
                      , write_file)
    elif command == "goodbye":
        return
    else:
        speak("sorry_i_dont_know_that_command")


while True:
    input = listen()
    if has_attention == False:
        if input == callsign:
            has_attention = True
            speak(greetings())
    else:
        if input != "force stop":
            command_center(input)

