import speech_recognition as sr
from aristotle_voice import *

class Voice:
    def __init__(self):
        self.r = sr.Recognizer()


    def listen(self):
        # obtain audio from the microphone
        with sr.Microphone() as source:
            print("Say something!")
            audio = self.r.listen(source)

        return audio


    def recogize_audio(self, audio):
        # recognize speech using Google Speech Recognition
        try:
            print("Aristotle thinks you said " + self.r.recognize_google(audio, show_all=False))
            return self.r.recognize_google(audio)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
            self.listen()
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))


    def get_audio(self):
        return self.recogize_audio(self.listen())
