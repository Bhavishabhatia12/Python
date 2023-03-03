import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import pyjokes
import datetime


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
print('here')
def talk(text):
    engine.say(text)
    engine.runAndWait()
talk("Hello, I am Alexa clone made by Bhavisha, how can I help you today?")

    # info = wikipedia.summary(person , 1)
    # print(info)
    # talk(info)

def take_command():
    listener = sr.Recognizer()
    with sr.Microphone() as source:
        print('listening...')
        voice = listener.listen(source)
    try:
        command = listener.recognize_google(voice)
        command = command.lower()
        if 'alexa' in command:
            command = command.replace('alexa', '')
            print(command)
        elif 'stop listening' in command or 'terminate' in command:
            print('Terminating program...')
            return None
    except:
        command = None
    return command

while True:
    command = take_command()
    if command is not None and 'play' in command:
        song = command.replace('play','')
        talk('playing'+song)
        pywhatkit.playonyt(song)
    elif command is not None and  'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is' +time)
    elif command is not None and  'date' in command:
        date = datetime.datetime.now().strftime('%Y-%m-%d')
        talk('Todays date is' +date)
    elif command is not None and 'who is' and 'where is' and 'what is'  in command:
         results = wikipedia.search(command)
         if len(results) == 0:
            print('No results found.')
         else:
            page = wikipedia.page(results[0])
            talk(page.summary)
         command = command.replace('who is', '')
         command = command.replace('where is', '')
         command = command.replace('what is', '')

         print(command)
    elif command is not None and  'date' in command:
        talk('sorry I have a boyfriend')
    elif command is not None and  'are you single' in command:
        talk('No I am in relationship with WIFI')
    elif command is not None and  'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('I could not recohnize the command')

    