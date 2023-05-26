from supporting_files.aristotle import Aristotle
from startup import Startup
import json
import argparse
import os

parser = argparse.ArgumentParser(description='An AI personal assistant that is specific to you.')

parser.add_argument("-g", "--Generate", help="A tool to generate a file based on the parameter given. OPTIONS: config - generates the configuration file.")
parser.add_argument("-d", "--Dependencies", help="Installs all nessecary dependencies to run the program. OPTIONS: install - installs all the pip packages.")

args = parser.parse_args()

if args.Generate == "config":
    hi = Startup()
    hi.startup_assist()

if args.Dependencies == "install":
    try:
        os.system("pip install -r \"dependencies.txt\"")
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
ari = Aristotle(config_file)
ari.main()