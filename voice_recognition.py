import speech_recognition as sr
from aristotle_voice import *


def listen():
    # obtain audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

    # recognize speech using Google Speech Recognition
    try:
        print("Google Speech Recognition thinks you said " + r.recognize_google(audio))
        return r.recognize_google(audio)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        listen()
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

