from supporting_files.aristotle import Aristotle
import json


# initializes a dictionary for the configuration file data
config_file = {}

with open("config.json", "r") as f:
    # the configuration data is loaded from the config file
    config_file = json.load(f)


# instantiate and run the bot!
# this instance uses the configuration file data
# this data is then distributed to all the other classes in this instances
ari = Aristotle(config_file)
ari.main()