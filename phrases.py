#List of phases Athena can use
import random


def greetings():
    lines = [
        "hello_there",
        "how_may_i_be_of_assistance",
        "greetings",
        "good_to_see_you"
    ]
    return random.choice(lines)



def responses():
    lines = [
        "sure_thing",
        "sure",
        "right_away",
        "processing",
        "most_definitely"
    ]
    return random.choice(lines)
