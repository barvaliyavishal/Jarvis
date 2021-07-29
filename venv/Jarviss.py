import speech_recognition as sr
import pyttsx3
from Commands import startJarvis,wishMe
import subprocess
import smtplib
from Help import checkInternetConnection, SpeakEngine

def takeCommand(flag=False):
    '''
    takeCommand take command from Michrophone 
    and return it in a form of string 
    '''

    #checking internet connection
    

    r = sr.Recognizer()

    with sr.Microphone() as source:         # use the default microphone as the audio source
        r.adjust_for_ambient_noise(source)  # here
        print("Listening...")
        audio = r.listen(source) 


    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print("Use said : ",query,"\n")
        return query
    except Exception as e:

        ### Check the internet Connection 
        # if False is checkInternetConnection.connect():
        #     SpeakEngine.speak("Sorry, No internet connection")
        if flag:
            SpeakEngine.speak("Sorry, I didn't get it. say That again please")
        return "None"
    

def mail(to):
    emaildictionary = Email.emailDict()
    if emaildictionary:
        if to in emaildictionary:
            SpeakEngine.speak("what should i say?")
            content = takeCommand()
            status = Email.sendEmail(to,content)
            if status:
                SpeakEngine.speak("email has been sent. Sir")
            else:
                SpeakEngine.speak("Something is Wrong Sir")

            
        else:
            msg = "there is no mail named " + to 
            SpeakEngine.speak(msg)
            SpeakEngine.speak("you can add new mail by saying: Jarvis Add new email")


def listen():
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'jarvis' in query:
            if 'jarvis quit' in query or 'jarvis shut down' in query or 'jarvis bye' in query:
                SpeakEngine.speak("Quitting sir, Thank you for your time, Have a good Day")
                break
            startJarvis(query)
        # elif 'jarvis' in query or 'hey jarvis' in query or 'hay jarvis' in query or 'oy jarvis' in query:
            # query = takeCommand(True).lower()
            

if __name__ == "__main__":
    if False is checkInternetConnection.connect():
            SpeakEngine.speak("Sorry, No internet connection")
    listen()
    