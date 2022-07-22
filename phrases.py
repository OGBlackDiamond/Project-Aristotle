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

def jokes(index):
    lines = [
        "why_did_the_chicken_cross_the_road",
        "what_is_green_and_has_wheels",
        "what_do_you_get_when_you_cross_a_bananna_and_a_shoe",
        "why_did_the_scarecrow_get_a_raise",
        "why_do_cows_have_bells"
    ]
    return lines[index]

def punchlines(index):
    lines = [
        "to_get_to_the_other_side",
        "grass_i_lied_about_the_wheels",
        "a_slipper",
        "it_was_out_standing_in_its_feild",
        "because_their_horns_dont_work"
    ]
    return lines[index]