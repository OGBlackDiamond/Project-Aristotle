from aristotle_voice import Response
from voice_recognition import Voice
from chat_responses import Chat
from phrases import *
import json

class Aristotle:
    def __init__(self):
        with open("callsign.json", "r") as f:
            self.callsign = json.load(f)
        with open("directive.json", "r") as f:
            self.directive = json.load(f)

        self.has_attention = False

        self.voice = Voice()
        self.chat = Chat()
        self.response = Response()

        self.input = ""

        self.ignore = 0



    def main(self):
        while True:
            self.input = self.voice.get_audio()
            if not self.entry_point(self.input) and self.has_attention == False:
                pass
                self.ignore += 1
            else:
                print("reached attention span")
                if self.dismiss(self.input):
                    self.has_attention = False
                if self.ignore < 0:
                    self.response.speak(self.command_center(self.input))
                self.ignore -=1


    def command_center(self, input):
        command = input
        print("reaching command center")
        if command == "change call sign":
            with open("callsign.json", "w") as write_file:
                json.dump(self.voice.get_audio(), write_file)
            return responses()
        elif command == "append to directive":
            self.response.speak("Sure thing. What would you like to add to the directive?")
            with open("directive.json", "w") as write_file:
                json.dump(self.directive + self.voice.get_audio()+ ". ", write_file)
            return "Directive Updated!"
        else:
            return self.chat.getChat(f"{self.directive}Caden tells you {input}, what do you say?")


    def entry_point(self, input):
        if input == self.callsign:
            self.response.speak(greetings())
            self.has_attention = True
            return True
        else:
            return False
                
    def dismiss(self, input):
        if input != 'goodbye':
            pass
        else:
            self.response.speak(goodbyes())
            return True

ari = Aristotle()
ari.main()