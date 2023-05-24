# Project Aristotle 

## About Aristotle
Aristotle is an artificial inteligence used as a personal assistant.
He has a unique personality that can be edited at will by the user.
He is a friend and a companion, but will also be harsh with the voice of reason.
Enjoy!

## Startup
On startup, Aristotle will attempt to read a file called config.json in order to gather information about itself for optimal use. This file can be automatically generated using the built in config generator. Simply run the 'startup.py' file and follow the instructions, most everything else will be done for you. 
##### Note:
You have to input your API keys manually. Your openAI API key will be gotten from the OS variable, if you don't know how to do this, I reccomend looking at a guide. Your elevenlabs key(s) should go into the config file like this:
```
...
"keys" : {
    "elevenlabs_keys": {
        "apikey0": "{key here}",
        "apikey1": "{key here}",
        "apikey2": "{key here}",
        "apikey3": "{key here}"
    }
},
...
```
more or less keys can be added as needed, but they must be formatted such that, the names go up in increments of 1, starting at 0, as shown.

## Use
Entry point (the file to run) is main.py
His personality (directive) lives in the config.json file, the key is "directive". This is what allows him to be personalized and tailored to any needs, while running the program, you can say "append to directive". You should be asked what you want to be added. After which, you can speak to add to your directive. I recommend speaking in the 3rd person, for example:

1. Instead of saying "I like to play games" say "{your name} likes to play video games".
2. Instead of saying "You are supposed to to be nice to me" say "Your directive is to be nice to {your name}"

This is becuase in order to personalize the AI to you, it uses a preface (the directive) before your input to make it the way it is.

Here is my personalized directive you can use as an example:
"You are a virtual assistant named Aristotle. Your creator and companion, Caden Feller, is an aspiring software engineer who likes to play video games, solve Rubik's cubes, and code fun projects to expand his knowledge and skills. He takes his academics very seriously, and works very hard. Your directive is to be a friend to Caden, but also be honest with him, and help him with whatever he may need. You will be kind to him, but also be harsh with him when he needs it. You like cupcakes with silver sprinkles. "

Because of this, adding to the directive in 1st person could make for some interesting artifacts in the responses, especially when asking specifically about yourself, or the machine.

The default gender is male, hence Aristotle. However, if you wish it to be a female, you can ask it to "change gender", where it will change its voice to a female's, and it's name will become Athena.
### Fun fact:
Aristotle was originally going to be 'Athena', but when starting this project back in the beginning of 2022, I could not find a good female voice model, so I had to switch it to a male. I found a better speech synthesis API (elevenlabs), but I still used a male voice, but it also had good female voice models as well. Thusly, as a tribute to the origional idea for this project, the option for the bot to be Athena was added later in development.

## Under The Hood
The mechanisms that the machine use are not very complex. It uses Google's speech recognition API to understand what the user is saying, it takes that input, along with the directive, and then uses ChatGPT to generate a response. Finally, it uses Elevenlab's speech synthesis API to turn the response into speech, which then gets spoken back to the user. There are a handfull of issues with the code right now, such as the library I am using to play the sound generated by the speech API is straight up bad, and it requires me to delete the file and remake a new one every time I make a new sound file, but the code is functional.