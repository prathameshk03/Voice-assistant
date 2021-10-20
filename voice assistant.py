import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)       #giving alexa female voice (index 0 for male)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:         #using microphone as source of audio or command
            print('listening...')    
            voice = listener.listen(source)
            command = listener.recognize_google(voice)      #google gives text of the audio
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa','')       #removes word alexa from our sentence
                print(command)
    except:
        pass
    return command
  
  
def run_alexa():
    command = take_command()        #take command from user
    print(command)
    
    if 'hi' in command:
        talk('hello! i am alexa! what can i do for you?')
    elif 'play' in command:
        song = command.replace('play','')        #replace 'play' with empty string
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')     #%H in place of %I gives 24 hr format
        talk('Current time is ' + time)
    elif 'search' in command:
        result = command.replace('search','')
        info = wikipedia.summary(result, 1)                 #one line summary
        print(info)
        talk(info)
    elif 'date' in command:
        date = datetime.datetime.now().strftime('%A, %dth %B, %Y')
        talk('Today is ' + date)    
    elif 'joke' in command:
        talk(pyjokes.get_joke(language='en',category='all'))
    elif 'repeat after me' in command:
        command = command.replace('repeat after me','')
        talk(command)
    elif 'goodbye' in command:
        talk('goodbye')
        exit()                                  #exit code
    else:
        talk('Sorry I didn\'t understand.')
        
while True:
    run_alexa()
    