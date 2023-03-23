from aristotle_voice import Response
from voice_recognition import Voice
from chat_responses import Chat
from phrases import *
import json

"""
The main class that handles all the logic to make the 
bot itself. 
"""
class Aristotle:
    def __init__(self):

        #initalize the callsign and directive variables
        with open("config.json", "r") as f:
            self.callsign = json.load(f)["callsign"]
            self.directive = json.load(f)["directive"]

        # instantiate classes for use
        self.voice = Voice()
        self.chat = Chat()
        self.response = Response()


        # assorted variable definition
        self.input = ""

        self.ignore = 0

        self.has_attention = False


    """
    the main method, compiles everything into one loop
    all methods from every class are referenced in one 
    way or another here
    """
    def main(self):
        while True:
            # gets input from the user
            self.input = self.voice.get_audio()
            #checks if the bot is at attention
            if not self.entry_point(self.input) and self.has_attention == False:
                continue
                #self.ignore += 1
            else:
                # if the bot does have attention, run it through the command center
                print("reached attention span")
                if self.dismiss(self.input):
                    self.has_attention = False
                #if self.ignore < 0:
                self.response.speak(self.command_center(self.input))
                #self.ignore -=1


    # use this method if you want a text based interface
    def simulateSpeech(self, input):
        self.response.speak(self.command_center(input)) 


    # the method that will chaeck for dedicated commands
    # if no command is found, it will run it through ChatGPT and the direcive
    def command_center(self, input):
        command = input
        print("reaching command center")
        # checks for commands
        if command == "append to directive":
            self.response.speak("Sure thing. What would you like to add to the directive?")
            self.appendToDirective(self.voice.get_audio())
            return "Directive Updated!"
        elif command == "change gender" or "change personality":
            self.switchGender()
            return "Good to be back!"
        # if no command is present, it will run through ChatGPT with the directive as input
        else:
            return self.chat.getChatTurbo(f"{self.directive}Caden tells you {input}, what do you say?")

    # the 'entry point', this method checks if the bot's attention is needed
    def entry_point(self, input):
        if input == self.callsign:
            self.response.speak(greetings())
            self.has_attention = True
            return True
        else:
            return False

    # the 'exit point', checks if the bot's attention is no longer needed
    def dismiss(self, input):
        if input != 'goodbye':
            pass
        else:
            self.response.speak(goodbyes())
            return True


    # switches the gender from male to female (trans robot rights!)
    def switchGender(self):
        file = {}
        with open("config.json", "r") as f:
            file = json.load(f)

        with open("config.json", "w") as f:
            if file["callsign"] == "Aristotle":
                file["callsign"] = "Athena"
                file["gender"] = "female"
            elif file["callsign"] == "Athena":
                file["callsign"] == "Aristotle"
                file["gender"] = "male"
            json.dump(file, f, indent=4)

    # appends to the directive based on input
    def appendToDirective(self, input):
        file = {}
        with open("config.json", "r") as f:
            file = json.load(f)

        with open("config.json", "w") as f:
            file["directive"] += f"{input}. "

    # test method, nothing special goes here
    def test(self, input):
        self.response.speak(self.chat.getChatBabbage(f"{self.directive}Caden tells you {input}, what do you say?"))

# instantiate and run the bot!
ari = Aristotle()
ari.main()