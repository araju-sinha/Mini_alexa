import datetime

import pyjokes
import speech_recognition as sr
import pyaudio
import pyttsx3
#import pywhatkit
import wikipedia

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
# engine.say("Hey! what can i do for you Aarju !!!!!")
# engine.runAndWait()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def alexa_listen():
    try:
        with sr.Microphone() as source:
            print("Listning...............")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
            else:
                talk("Give me command again..... can't process")
    except:
        pass
    return command

def run_alexa():
    command = alexa_listen()
    if 'play' in command:
        song = command.replace('play', '')
        talk("Playing.." + song)
        #pywhatkit.playonyt(song)
    elif 'math' in command:
        solve = command.replace('math', '')
        talk("2plus2is4")
    elif 'tell' in command:
        info = command.replace('tell', '')
        detl = wikipedia.summary(info, 1)
        talk("Information abt " + info)
        print (detl)
    elif 'date' in command:
        today_date = datetime.datetime.now().strftime('%I:%M %p')
        t_date = today_date.day + today_date.month  + today_date.year
        talk("Current date is " + t_date)
        print("Current date is : " + t_date)
    elif 'time' in command:
        today_time = datetime.datetime.now().strftime('%I:%M %p')
        t_time = today_time.hour + today_time.minute + today_time.second
        talk("Current time is " + t_time)
        print("Current time is : " + t_time)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif '' in command:
        talk("can't hear......")
        quit()
    else:
        print("No commands")


while True:
    run_alexa()




