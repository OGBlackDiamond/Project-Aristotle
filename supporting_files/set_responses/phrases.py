#List of phases Aristotle can use
import random

"""
This file defines a bunch of pre-programmed responses for 
the bot to say when needed or requested
"""

def greetings():
    lines = [
        "hello there",
        "how may i be of assistance",
        "greetings",
        "good to see you",
        "Hello Caden. I'm here to help with whatever you need"
    ]
    return random.choice(lines)


def responses():
    lines = [
        "sure thing",
        "sure",
        "right away",
        "processing",
        "most definitely"
    ]
    return random.choice(lines)


def goodbyes():
    lines = [
        "goodbye, Caden",
        "see you next time",
        "stay fresh!"
    ]
    return random.choice(lines)