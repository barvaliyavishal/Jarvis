import pyttsx3
engine = pyttsx3.init()
engine.setProperty('rate',160)
    

def speak(audio):
    '''
        implementation of speak fnction 
        which takes text as an argument
        and convert int into speech and speak.
    '''

    voices = engine.getProperty('voices')
    # engine.setProperty('voice',voices[1].id)
    engine.say(audio)
    engine.runAndWait()