from supporting_files.speech import Speech
from supporting_files.voice import Voice
from supporting_files.chat import Chat
from supporting_files.set_responses.phrases import *
import json

"""
The main class that handles all the logic to make the 
bot itself. 

This class takes in the configuration data
and distributes it to the rest of the classes
when they are instantiated.

Additionally, it acts as the main passthrough for all
classes and their methods, as well as any otherwise
defined functions.
"""
class Aristotle:

    def __init__(self, config_data):

        # uses the configuration data passed in by main.py
        # to assign all of the necessary variables for use and distribution

        #variable to determine the user's name
        self.user_name = config_data["user_name"]
        # variable to determine the name
        self.callsign = config_data["callsign"]
        # variable to determine the gender
        self.gender = config_data["gender"]
        # variable to acknowledge the directive
        self.directive = config_data["directive"]
        self.directive = self.directive.replace('<user_name', self.user_name)
        self.directive = self.directive.replace('<callsign>', self.callsign)
        self.directive = self.directive.replace('<gender>', self.gender)
        # variable to determine the interaction mode
        self.mode = config_data["interaction_mode"]
        # dictionary containing all of the API keys
        self.keys = config_data["data"]["keys"]
        # dictionary containing all of the request URLs
        self.urls = config_data["data"]["request_urls"]


        # instantiate classes with the necessary data from the configuration file
        self.speech = Speech(self.keys, self.urls)
        self.chat = Chat(self.urls, self.directive)
        self.voice = Voice()

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
            # gets input from the user, depending on the interaction mode
            if self.mode == "speech":
                #gets audio input
                self.input = self.voice.get_audio()
            elif self.mode == "text":
                # gets text input
                self.input = input("Type something ::\n")
                self.has_attention = True
            else:
                # default input is an empty string
                self.input = ""

            # breaks the loop on request
            if self.input == "force stop":
                break

            #checks if the bot is at attention
            if self.has_attention == False:
                self.entry_point(self.input)
            else:
                # if the bot does have attention, run it through the command center
                if self.dismiss(self.input):
                    continue
                self.speech.speak(self.command_center(self.input), self.gender)


    # the method that will check for dedicated commands
    # if no command is found, it will run it through ChatGPT and the directive
    def command_center(self, input):
        command = input
        # checks for commands

        # appends a new personality trait to the directive
        if command == "append to directive":
            self.speech.speak("Sure thing. What would you like to add to the directive?", self.gender)
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
            return self.chat.get_chat_turbo(f"{self.user_name} tells you {input}.")

    # the 'entry point', this method checks if the bot's attention is needed
    def entry_point(self, input):
        if input == self.callsign:
            self.speech.speak(greetings(), self.gender)
            self.has_attention = True
            return True
        else:
            return False

    # the 'exit point', checks if the bot's attention is no longer needed
    def dismiss(self, input):
        if input == 'goodbye':
            self.chat.summarize_conversation()
            self.chat.clear_messages()
            self.speech.speak(goodbyes(), self.gender)
            self.has_attention = False
            return True
        else:
            return False


    # switches the gender from male to female, or vice versa (trans robot rights!)
    def switch_gender(self):
        file = {}
        with open("config.json", "r") as f:
            file = json.load(f)
        # checks if the current name is Aristotle(male), if it is, switch it to Athena(female)
        if self.callsign == "Aristotle":
            file["callsign"] = "Athena"
            file["gender"] = "female"
        # checks if the current name is Athena(female), if it is, switch it to Aristotle(male)
        elif self.callsign == "Athena":
            file["callsign"] = "Aristotle"
            file["gender"] = "male"

        self.callsign = file["callsign"]
        self.gender = file["gender"]

        # write the new data back to the config file so it can be saved in the event of a reboot
        with open("config.json", "w") as f:
            json.dump(file, f, indent=4)


    # switches the interaction mode between speech (talking) and text (typing)
    def switch_interaction_mode(self):
        file = {}
        with open("config.json", "r") as f:
            file = json.load(f)

        # checks if the current mode is speech, if it is switch it to text
        # if it isn't, switch it to speech
        if self.mode == "speech":
            self.mode = "text"
        else:
            self.mode = "speech"

        file["interaction_mode"] = self.mode

        # write the new data back to the config file so it can be saved in the event of a reboot
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
            json.dump(file, f, indent=4)


    # test method, nothing special goes here
    def test(self, input):
        self.speech.speak(self.chat.get_chat_curie(f'{self.directive}{self.user_name} tells you "{input}", what do you say?', self.gender))
