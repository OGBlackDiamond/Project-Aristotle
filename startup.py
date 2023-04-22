import os
import json
# this class will assist the user in creating their virtual assistant
class Startup:
    def __init__(self):
        self.config = {}
        self.input = ""
        self.callsign = ""
        self.gender = ""
        self.directive = ""
        self.interaction_mode = ""

    def startup_assist(self):
        self.check_config_exists()
        print("Welcome! You almost have your personalized assistant ready to go!")
        print("First, we need to configure a couple things before you get started.")
        self.set_name()
        self.set_gender()
        self.set_interaction_mode()
        print("Now comes the hard part.")
        self.set_directive()
        print("Amazing! Let me make sure I got this all correct.")
        while self.check_if_correct():
            pass





    def check_config_exists(self):
        if os.path.exists("config.json") :
            self.input = input("You already have a configuration file, do you want to delete it and start again? (y/n)\n")
            while self.input != "y" and self.input != "n" :
                self.input = input("Response not applicable, 'y' or 'n' expected\n")

            if self.input == "y":
                print("Okay! Starting from scratch. Goodbye!\n\n")
            elif self.input == "n":
                print("\nOkay! Your current assistant will stay.")
                print("If you are trying to run the assistant, I would reccomend the main.py file!")

    def set_name(self):
        self.callsign = input("What would you like to call your assistant?\n")
        print(f"\nOkay! Your assistant's name will be {self.callsign}!")

    def set_gender(self):
        self.gender = input("How does your assistant identify? (male, female, non-binary, etc)\n")
        print(f"\nSounds good! Your assistant identifies as {self.gender}")

    def set_interaction_mode(self):
        print("\nWhat would you like your default interaction mode to be?")
        self.interaction_mode = input("(text / speech) text is interaction via typing, speech is interaction via your voice\n")
        while self.interaction_mode != "text" and self.interaction_mode != "speech":
            self.interaction_mode = input("\nResponse not applicable, 'text' or 'speech' expected\n")
        print(f"\nGreat! Your defualt interaction mode is {self.interaction_mode}")

    def set_directive(self):
        print("\nYou must describe the assistant's purpose. I recommend looking at the README file on github before proceeding any further.")
        self.directive = input("So, what will it's purpose be?\n")

    def list_attributes(self):
        print(f"\nYour assistant's name is - {self.callsign}")
        print(f"\nYour assistant identifies as - {self.gender}")
        print(f"\nYour default interaction mode is - {self.interaction_mode}")
        print(f"\nAnd last but not least, your assistant's purpose is - {self.directive}")

    # TODO:make default config file
    def write_to_file(self):
        self.config = {
            "callsign": self.callsign,
            "directive": self.directive,
            "gender": self.gender,
            "interaction mode": self.interaction_mode,
            "data": {
                "keys": {
                    "elevenlabs_keys": {}
                },
                "request_urls": {
                    "aristotle_url": "https://api.elevenlabs.io/v1/text-to-speech/pNInz6obpgDQGcFmaJgB",
                    "athena_url": "https://api.elevenlabs.io/v1/text-to-speech/EXAVITQu4vr4xnSDxMaL",
                    "subscription_url": "https://api.elevenlabs.io/v1/user/subscription",
                    "chat_completions_url": "https://api.openai.com/v1/chat/completions",
                    "completions_url": "https://api.openai.com/v1/completions"
                }
            }
            }

        with open("config.json", "w") as f:
            json.dump(self.config, f, indent=4)

    def check_if_correct(self):
        self.list_attributes()
        self.input = input("\nDoes this look correct? (y/n)\n")
        while self.input != "y" and self.input != "n" :
            self.input = input("Response not applicable, 'y' or 'n' expected\n")
        if self.input == "y":
            print("\nOkay! Lets get this party started!")
            self.write_to_file()
            print("Please add your API keys to the file, as per the instructions in the README file.")
            return True
        elif self.input == "n":
            print("\nbruh moment")
            self.input = input("\nWhat do you want changed? (name/gender/interaction mode/directive)\n")
            while self.input != "name" and self.input != "gender" and self.input != "interaction mode" and self.input != "directive":
                self.input = input("Response not applicable, 'name', 'gender', 'interaction mode', or 'directive' expected\n")
            if self.input == "name":
                self.set_name()
            elif self.input == "gender":
                self.set_gender()
            elif self.input == "interaction mode":
                self.set_interaction_mode()
            elif self.input == "directive":
                self.set_directive()
            return False




hi = Startup()
hi.startup_assist()