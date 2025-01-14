import text_to_speech
import speech_to_text
import datetime
import webbrowser
def Action(data):
    user_data= data.lower()
    if "what is your name" in user_data:
            text_to_speech.text_to_speech("My name is robo")
            return "My name is robo"

    elif "hello" in user_data or "hey robo" in user_data:
        text_to_speech.text_to_speech("hello,how can i help you")
        return "hello,how can i help you"

    elif "good morning" in user_data:
        text_to_speech.text_to_speech("good morning sir")
        return "good morning sir"
    elif "good night" in user_data:
        text_to_speech.text_to_speech("good night sir")
        return "good night sir"

    elif "date and time" in user_data:
        current_time=datetime.datetime.now()
        Time=(str)(current_time)+"Hour :",(str)(current_time.minute)+"Minute"
        text_to_speech.text_to_speech(Time)
        return Time
    
    elif "shutdown" in user_data:
        text_to_speech.text_to_speech("ok sir")
        return "ok sir"

    elif "play music" in user_data:
        webbrowser.open("http://spotifysong01.freewebhostmost.com/")
        text_to_speech.text_to_speech("enjoy music")
        return "enjoy music"

    elif "open youtube" in user_data:
        webbrowser.open("https://www.youtube.com/")
        text_to_speech.text_to_speech("youtube opened")
        return "youtube opened"

    elif "open google" in user_data:
        webbrowser.open("https://www.google.co.in/")
        text_to_speech.text_to_speech("google opened")
        return "google opened"
    
    elif "open linkedin" in user_data:
        webbrowser.open("https://www.linkedin.com/in/puskar-jana-798502316/")
        text_to_speech.text_to_speech("linkedin opened")
        return "linkedin opened"
    
   
    else:
        text_to_speech.text_to_speech("sorry sir i can't understand what you are saying")
        return "sorry sir i can't understand what you are saying"

