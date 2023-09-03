# Project Aristotle 

## About Aristotle
Aristotle is an artificial intelligence used as a personal assistant. His objective is to do something that a virtual assistant can't do yet. While Aristotle can't interact with your OS (yet), he can interact with you on a more emotional level. He is designed to be a friend over a tool, meaning that he can't edit files for you, but he can still provide useful information upon request, and give you advice, interact with you like a person would, etc. 
<br /><br />
A major point that will set Aristotle apart from other personal assistants, is his memory, the hard part of this project. (When development finishes) Aristotle can remember conversations hes had in the past, and use them to provide better user experiences in the future.
## Startup
To install all dependencies needed for Aristotle to run, open your command line in the aristotle directory, and run the following command:
```python3 main.py -d install```. If you run into issues, you can open the dependencies.txt file, and manually install each package.

On startup, Aristotle will attempt to read a file called config.json in order to gather information about itself for optimal use. This file can be automatically generated using the built in configuration utility. Simply run the following command: ```python3 main.py -g config```, and follow the instructions, most everything else will be done for you.

##### Note:
The configuration utility should allow you to input your API keys, in the event you don't want to use the utility, you will have to enter your keys manually. Your openAI API can be accessed from either the OS variable (if you don't know how to do this, I recommend looking at a guide) OR a value in the configuration file. Your key(s) should go into the config file like this:
```
...
"keys" : {
    "elevenlabs_keys": {
        "key0": "{key here}",
        "key1": "{key here}",
        "key2": "{key here}",
        "key3": "{key here}"
    },
    "openai_key": "key optionally here"
},
...
```
more or less elevenlabs keys can be added as needed, but they must be formatted such that the names go up in increments of 1, starting at 0, as shown.

## Use
Entry point (the file to run) is main.py
His personality (directive) lives in the config.json file, the key is "directive". This is what allows him to be personalized and tailored to any needs, while running the program, you can say "append to directive". You should be asked what you want to be added. After which, you can speak to add to your directive. I recommend speaking in the 3rd person, for example:

1. Instead of saying "I like to play games" say "{your name} likes to play video games".
2. Instead of saying "You are supposed to to be nice to me" say "Your directive is to be nice to {your name}"

This is because in order to personalize the AI to you, it uses a preface (the directive) before your input to make it the way it is.

Here is my personalized directive you can use as an example:
"You are a virtual assistant named <callsign>. Your creator and companion, <user_name>, is an aspiring software engineer who likes to play video games, solve Rubik's cubes, and code fun projects to expand his knowledge and skills. He takes his academics very seriously, and works very hard. Your directive is to be a friend to <user_name>, but also be honest with him, and help him with whatever he may need. You will be kind to him, but also be harsh with him when he needs it. You like cupcakes with silver sprinkles. "

Because of this, adding to the directive in 1st person could make for some interesting artifacts in the responses, especially when asking specifically about yourself, or the machine.

The default gender is male, hence Aristotle. However, if you wish it to be a female, you can ask it to "change gender", where it will change its voice to a female's, and its name will become Athena.
### Fun fact:
Aristotle was originally going to be 'Athena', but when starting this project back in the beginning of 2022, I could not find a good female voice model, so I had to switch it to a male. I found a better speech synthesis API (elevenlabs), but I still used a male voice, but it also had good female voice models as well. Thusly, as a tribute to the original idea for this project, the option for the bot to be Athena was added later in development.

## Under the Hood
The mechanisms that the machine use are not very complex. It uses Google's speech recognition API to understand what the user is saying, it takes that input, along with the directive, and then uses ChatGPT to generate a response. Finally, it uses Elevenlab's speech synthesis API to turn the response into speech, which then gets spoken back to the user. There are a handful of issues with the code right now, such as the library I am using to play the sound generated by the speech API is straight up bad, and it requires me to delete the file and remake a new one every time I make a new sound file, but the code is functional.

## Under the Hood - Deep Dive
### Configuration Utility
The configuration utility (startup.py) is used to assist the user in creating the *config.json*, where all of the data about Aristotle (besides memory) is held. The configuration file needs the users name, Aristotle's name (changes based on gender), the directive (base personality), gender (changes with the voice and name between male and female), and interaction mode (text or speech). These values define the way that Aristotle interacts with the user. There is also a data subsection that contains all of the urls that need to be used to make requests to the various APIs utilized in this project. It also contains a keys section that will house all of the users API keys, such as elevenlabs keys, (more than one optional) and an OpenAI key (optionally can be accessed from the operating system variable). The URLs cannot be configured by the user, as the urls remain static no matter the implimentation. The configuration utility essentially provides a TUI to help the user create this file, and automatically format it for the user. It uses python's basic input() function to gather input, after prompting the user for the specific piece of information. If input requires a specific format, it will reject that input until the format is met.
### The Entry Point
The entry point (main.py) is a file that allows all functionality to be accessed. Running it normally will boot up Aristotle for business as usual. However, it also contains an arguement parser to allow further functionality. You can use the configuration utility by running *main.py*, but also adding  '-g' (generate flag) and 'config' (configuration parameter). Additionally, you can install all dependencies by adding the '-d' (dependencies flag) and 'install' (install parameter). The second use case is slightly excessive, but I wanted to learn how to use an argument parser and wanted to have more than one implimentation. Mainly, this is future-proofing for when this project gets bigger. When running the *main.py* file vanilla, it will simply read data from the configuration file, and instantate an Aristotle class.
### Aristotle
*Aristotle.py* is the file where most of the logic exists. It is the file that compiles all other classes from all other files into a working product. In the constructor, it will take the configuration file passed in, and populate all of the instance variables with that data. This includes name, gender, interaction mode, directive, etc. It will also instantiate other supporting files, and pass in the data that they need to function. For example, the chat class makes requests to the OpenAI api, so it needs those urls, it needs the API keys to make the request, it needs the directive to pass in as input, and it needs Aristote's name, for input. All of this is passed into that class so it can be used when making that request.
<br /><br />
When using the voice interface, you don't always want Aristotle to respond to whatever you're saying in the event that you aren't a nerd and actually have other people in your life to talk to. Because of this, a variable is used to determine if Aristotle's attention is needed. Aristotle will always be listening, but will only respond if his name is spoken, like most other virtual assistants that exist today. After this, Aristotle will respond to anything that is spoken, because it will assume that you're talking to it. When you don't want Aristotle to respond to what you're saying, you can say 'goodbye' after which he will wish you well and listen for only his name.
<br /><br />
When interacting with Aristotle, it will check your input for any dedicated commands first (i.e. change gender, switch interaction mode, etc.) if one isn't found, it will use your input as a prompt for a response, using ChatGPT. More information about this process can be found in the chat section.
<br /><br />
Other methods here are commands, many of which are altering the configuration file.
### Speech
The *speech.py* class simply uses the Google Speech Recognition API and returns the text input. I'm pretty sure I copy pasted the example code from their documentation and changed two thing. This class is not very complex, nothing big to say about it.
### Voice
The *voice.py* class handles the response portion of Aristotle. Meaning, whenever we get a response from the chat section, this is how Aristotle talks back to you. The logic present is not very complex. It makes requests to the Elevenlabs API, and contains some additional logic to juggle API keys if more than one are being used, to allow even distribution of the limited tokens. Nothing too special here.
### Chat
As the name implies, the *chat.py* class handles all requests to the OpenAI API. I
