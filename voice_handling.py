from athena_voice import *
from voice_recognition import *
with open("callsign.json", "r") as f:
        callsign = json.load(f)





        
def command_center():
    if listen() == callsign:
        speak("hi_there")
        speak("how_can_i_help")
        command = listen()
        if command == "repeat after me":
            words = ""
            while words != "stop":
                speak(words)
                words = listen()
        elif command == "tell me a joke":
            print()
        elif command == "change callsign":
            speak("sure")
            speak("what would you like my new call sign to be")
            with open("callsign.json", "w") as write_file:
                json.dump(listen(), write_file)

