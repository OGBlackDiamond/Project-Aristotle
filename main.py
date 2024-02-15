#! python3
from startup import Startup
import json
import argparse
import os

parser = argparse.ArgumentParser(description='An AI personal assistant that is specific to you.')

parser.add_argument("--generate_config",action="store_true", help="Generates the configuration file.")
parser.add_argument("--install_dependencies", action="store_true", help="Installs all the pip packages that this program depends on.")

args = parser.parse_args()

if args.generate_config:
    startup = Startup()
    startup.startup_assist()

if args.install_dependencies:
    try:
        os.system("pip install -r \"requirements.txt\"")
        print("\n\nSuccessfully installed all packages!")
    except:
        print("Packages could not be installed! Please install them manually.")
    quit()

# initializes a dictionary for the configuration file data
config_file = {}

with open("config.json", "r") as f:
    # the configuration data is loaded from the config file
    config_file = json.load(f)


# instantiate and run the bot!
# this instance uses the configuration file data
# this data is then distributed to all the other classes in this instances
from supporting_files.aristotle import Aristotle
ari = Aristotle(config_file)
ari.main()