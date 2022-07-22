from aristotle_voice import *
from voice_recognition import *
from phrases import *
import random
with open("callsign.json", "r") as f:
        callsign = json.load(f)





        
def command_center():
    command = listen()
    if command == "repeat after me":
        words = ""
        while words != "stop":
            speak(words)
            words = listen()
    elif command == "introduce yourself":
        speak("hello")
        speak(f"my_name_is_{callsign}")
    elif command == "tell me a joke":
        num = int(random.random()*10)
        while num > 4:
            num = int(random.random()*10)
        speak(jokes(num))
        speak(punchlines(num))
    elif command == "change call sign":
        speak(responses())
        speak("what_would_you_like_my_new_call_sign_to_be")
        with open("callsign.json", "w") as write_file:
            json.dump(listen().lower(), write_file)
    elif command == "bye":
        return
    else:
        speak("sorry_i_dont_know_that_command")

    command_center()

speak(greetings())
command_center()