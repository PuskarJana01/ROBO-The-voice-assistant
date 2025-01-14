import pyttsx3

engine = pyttsx3.init()
engine.say("robo started")
engine.runAndWait()

def text_to_speech(text):
    engin=pyttsx3.init()
    rate=engin.getProperty('rate')
    engin.setProperty('rate','rate-70')
    engin.say(text)
    engin.runAndWait()

