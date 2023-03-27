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

        #initalize the callsign, directive, gender and mode variables
        with open("config.json", "r") as f:
            file = json.load(f)
            # variable to deterine the name
            self.callsign = file["callsign"]
            # variable to determine the gender
            self.gender = file["gender"]
            # variable to aknowledge the directive
            self.directive = file["directive"]
            self.directive = self.directive.replace('<callsign>', self.callsign)
            self.directive = self.directive.replace('<gender>', self.gender)

            # variable to determine the interaction mode
            self.mode = file["interaction mode"]


        # instantiate classes for use
        self.voice = Voice()
        self.chat = Chat()
        self.response = Response()

        # the variable that will control whether Aristotle will respond to input
        self.has_attention = False

        # assorted variable definition
        self.input = ""






    """
    the main method, compiles everything into one loop
    all methods from every class are referenced in one 
    way or another here
    """
    def main(self):
        while True:
            # gets input from the user
            if self.mode == "speech":
                self.input = self.voice.get_audio()
            elif self.mode == "text":
                self.input = input("Type something ::\n")
                self.has_attention = True
            else:
                self.input = ""

            # breaks the loop on request
            if self.input == "force stop":
                break

            #checks if the bot is at attention
            if not self.entry_point(self.input) and self.has_attention == False:
                continue
            else:
                # if the bot does have attention, run it through the command center
                if self.dismiss(self.input):
                    self.has_attention = False
                self.response.speak(self.command_center(self.input), self.gender)


    # the method that will check for dedicated commands
    # if no command is found, it will run it through ChatGPT and the directive
    def command_center(self, input):
        command = input
        # checks for commands

        # appends a new personality trait to the directive
        if command == "append to directive":
            self.response.speak("Sure thing. What would you like to add to the directive?", self.gender)
            self.append_to_directive(self.voice.get_audio())
            return "Directive Updated!"
        # switches between Aristotle and Athena
        elif command == "change gender" or command == "change personality":
            self.switch_gender()
            return "Good to be back!"
        # changes the interaction from speech to text and vice versa
        elif command == "change interaction mode":
            self.switch_interaction_mode()
        # if no command is present, it will run through ChatGPT with the directive as input
        else:
            return self.chat.get_chat_turbo(f"{self.directive}Caden tells you {input}, what do you say?")

    # the 'entry point', this method checks if the bot's attention is needed
    def entry_point(self, input):
        if input == self.callsign:
            self.response.speak(greetings(), self.gender)
            self.has_attention = True
            return True
        else:
            return False

    # the 'exit point', checks if the bot's attention is no longer needed
    def dismiss(self, input):
        if input != 'goodbye':
            pass
        else:
            self.response.speak(goodbyes(), self.gender)
            return True


    # switches the gender from male to female, or vice versa (trans robot rights!)
    def switch_gender(self):
        file = {}
        with open("config.json", "r") as f:
            file = json.load(f)

        self.callsign = file["callsign"]
        self.gender = file["gender"]

        if self.callsign == "Aristotle":
            file["callsign"] = "Athena"
            file["gender"] = "female"
        elif self.callsign == "Athena":
            file["callsign"] = "Aristotle"
            file["gender"] = "male"

        self.callsign = file["callsign"]
        self.gender = file["gender"]

        with open("config.json", "w") as f:
            json.dump(file, f, indent=4)



    def switch_interaction_mode(self):
        file = {}
        with open("config.json", "r") as f:
            file = json.load(f)
        self.mode = file["interaction mode"]

        if self.mode == "speech":
            self.mode = "text"
        else:
            self.mode = "speech"
        
        file["interaction mode"] = self.mode


        with open("config.json", "w") as f:
            json.dump(file, f, indent=4)

        return f"{self.mode} mode!"
        



        

    # appends to the directive based on input
    def append_to_directive(self, input):
        file = {}
        with open("config.json", "r") as f:
            file = json.load(f)

        with open("config.json", "w") as f:
            file["directive"] += f"{input}. "



    # test method, nothing special goes here
    def test(self, input):
        self.response.speak(self.chat.get_chat_curie(f"{self.directive}Caden tells you {input}, what do you say?", self.gender))
