import speech_recognition as sr

"""
This class will get the user's voice
This will be used as input
"""
class Voice:

    def __init__(self):
        self.r = sr.Recognizer()

    # listen to the user
    def listen(self):
        # obtain audio from the microphone
        with sr.Microphone() as source:
            print("Say something!")
            audio = self.r.listen(source)

        return audio

    # find speech in the audio
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

    # return the test from the speech
    def get_audio(self):
        return self.recogize_audio(self.listen())

