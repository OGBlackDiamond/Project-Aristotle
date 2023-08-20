import os
import json
# this class will assist the user in creating their virtual assistant
class Startup:
    # initializes variables that will go into the configuration file
    def __init__(self):
        self.config = {}
        self.user_name = ""
        self.input = ""
        self.callsign = ""
        self.gender = ""
        self.directive = ""
        self.interaction_mode = ""
        self.elevenlab_keys = {}
        self.openai_key = ""

    # assists the user in starting their assistant
    def startup_assist(self):
        self.check_config_exists()
        print("Welcome! You almost have your personalized assistant ready to go!")
        print("First, we need to configure a couple things before you get started.")
        self.get_username()
        if self.check_default_presets():
            self.write_to_file()
        else:
            self.set_gender()
            self.set_interaction_mode()
            print("Now comes the hard part.")
            self.set_directive()
            print("great. got keys?")
            self.set_api_keys()
            print("Amazing! Let me make sure I got this all correct.")
            while self.check_if_correct():
                pass
        print("Please ensure all the API key information is correct, and add any missing ones.")
        print("run the 'main.py' file to start your assistant after you have added your api keys.")
        quit()

    # checks if a configuration file already exists, and asks the user what action they would like to take
    def check_config_exists(self):
        if os.path.exists("config.json") :
            self.input = input("You already have a configuration file, do you want to delete it and start again? (y/n)\n")
            while self.input != "y" and self.input != "n" :
                self.input = input("Response not applicable, 'y' or 'n' expected\n")

            if self.input == "y":
                print("Okay! Starting from scratch. Goodbye!\n\n")
            elif self.input == "n":
                print("\nOkay! Your current assistant will stay.")
                print("If you are trying to run the assistant, I would recommend the main.py file!")
                quit()

    # checks if the user wants to use the default presets or not
    def check_default_presets(self):
        self.input = input("\nWould you like to use the default presets (y), or configure your own assistant? (n)\n")
        while self.input != "y" and self.input != "n":
            self.input = input("That's not a valid response.\nWould you like to use the default presets (y), or configure your own assistant? (n)\n")
        if self.input == "y":
            self.callsign = "Aristotle"
            self.gender = "male"
            self.directive = "Your directive is to be a helpful assistant"
            self.interaction_mode = "text"
            return True
        else:
            return False


    # this chunk of methods sets all of the attributes of the assistant

    def get_username(self):
        self.user_name = input("What is your name?\n")
        print(f"Got it, you are {self.user_name}")

    # gender
    def set_gender(self):
        self.gender = input("How does your assistant identify by default? (male, female)\n")
        while self.gender != "male" and self.gender!= "female":
            self.gender = input("\nNonbinary genders not applicable, 'male' or 'female' expected\n")
        print(f"\nSounds good! Your assistant identifies as {self.gender}")
        # sets the name of the assistant based on gender
        if self.gender == "male":
            self.callsign == "Aristotle"
        else:
            self.callsign == "Athena"

    # default interaction mode
    def set_interaction_mode(self):
        print("\nWhat would you like your default interaction mode to be?")
        self.interaction_mode = input("(text / speech) text is interaction via typing, speech is interaction via your voice\n")
        while self.interaction_mode != "text" and self.interaction_mode != "speech":
            self.interaction_mode = input("\nResponse not applicable, 'text' or 'speech' expected\n")
        print(f"\nGreat! Your default interaction mode is {self.interaction_mode}")

    # directive
    def set_directive(self):
        print("\nYou must describe the assistant's purpose. I recommend looking at the README file on github before proceeding any further.")
        self.directive = input("So, what will its purpose be?\n")

    # api keys
    def set_api_keys(self):
        self.input = input("would you like to add your api keys now? (y / n)\n")
        if self.input == "y":
            print("lets start with elevenlabs keys!\n")
            self.get_elevenlabs_keys()
            print("great! lets move on to your openai API key")
            self.get_openai_key()
        else:
            print("No worries! Just make sure you add your keys manually to the config file later.")

    # handles getting the elevenlabs keys
    def get_elevenlabs_keys(self):
        # keeps track of the key count
        key_count = 0

        self.input = input("Enter your first elevenlabs API key (press ENTER if you don't have one):\n")
        self.elevenlab_keys[f"key{key_count}"] = self.input
        while True:
            key_count += 1
            self.input = input("Do you have any more elevenlabs keys you would like to add? (y / n)\n")
            if self.input == "y":
                self.elevenlab_keys[f"key{key_count}"] = input("input your next key\n")
            else:
                break

    def get_openai_key(self):
        self.input = input("Input your openai API key (press ENTER if you don't have one):\n")
        self.openai_key = self.input


    # lists the current attributes for the user
    def list_attributes(self):
        print(f"\nYour assistant's name is - {self.callsign}")
        print(f"\nYour assistant identifies as - {self.gender}")
        print(f"\nYour default interaction mode is - {self.interaction_mode}")
        print(f"\nYour assistant's purpose is - {self.directive}")
        print(f"\nYour name is - {self.user_name}")

    # once the user has confirmed that everything is correct, it will write all of the data to a file
    def write_to_file(self):

        with open("template_config.json", "r") as f:
            self.config = json.load(f)
            f.close()

        self.config["user_name"] = self.user_name
        self.config["callsign"] = self.callsign
        self.config["gender"] = self.gender
        self.config["directive"] = self.directive
        self.config["interaction_mode"] = self.interaction_mode
        self.config["data"]["keys"]["elevenlabs_keys"] = self.elevenlab_keys
        self.config["data"]["keys"]["openai_key"] = self.openai_key

        with open("config.json", "w") as f:
            json.dump(self.config, f, indent=4)
            f.close()

    # checks if the input given is correct, and allows the user to edit their entries
    def check_if_correct(self):
        self.list_attributes()
        self.input = input("\nDoes this look correct? (y/n)\n")
        while self.input != "y" and self.input != "n" :
            self.input = input("Response not applicable, 'y' or 'n' expected\n")
        if self.input == "y":
            print("\nOkay! Lets get this party started!")
            self.write_to_file()
            return False
        elif self.input == "n":
            print("\nbruh moment")
            self.input = input("\nWhat do you want changed? (name/gender/interaction mode/directive/user name)\n")
            while self.input != "name" and self.input != "gender" and self.input != "interaction mode" and self.input != "directive" and self.input != "user name":
                self.input = input("Response not applicable, 'name', 'gender', 'interaction mode', 'directive', or 'user name' expected\n")
            if self.input == "name":
                self.set_name()
            elif self.input == "gender":
                self.set_gender()
            elif self.input == "interaction mode":
                self.set_interaction_mode()
            elif self.input == "directive":
                self.set_directive()
            elif self.input == "user name":
                self.get_username()
            return True
