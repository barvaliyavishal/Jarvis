
import wikipedia
import datetime
import webbrowser
from Help import SpeakEngine
import os
from playsound import playsound
from Help import Dictionary

def playSpotify():
    '''
    its used for grab the playlist from spotify

    '''
    import spotipy
    from spotipy.oauth2 import SpotifyClientCredentials

    birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'
    spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id="65628376760448d7bf8b556212f5f11c",client_secret="a32bf9520abb491a80d483439583c3c3"))

    results = spotify.artist_albums(birdy_uri, album_type='album')
    albums = results['items']
    while results['next']:
        results = spotify.next(results)
        albums.extend(results['items'])

    # for album in albums:
    #     print(album['name'])


def wishMe():
    '''
    Introduce jarvis and 
    wish to user based on time
    '''
    hour = int(datetime.datetime.now().hour)
    if hour < 12:
        SpeakEngine.speak("Good Morning sir")
    elif hour < 18:
        SpeakEngine.speak("Good Afternoon sir")
    else:
        SpeakEngine.speak("Good Evening sir")
    SpeakEngine.speak("I am Jarvis, how can i help you? ")


def startJarvis(query):
        '''
        this takes query which get from take command function and follow the comand
        '''





        ### greeting with Jarvis

        if 'jarvis' == query or 'jarvis are you there' in query or 'jarvis you are here' in query or 'jarvis are you here' in query:
            SpeakEngine.speak("Yes sir?")

        elif 'jarvis are you listening' in query or 'are you listening' in query:
            SpeakEngine.speak("Yes sir, i am listening")

        elif 'who are you' in query:
                SpeakEngine.speak("i name is jarvis. i am a virtual assistant")
        
        elif 'can you help me' in query or 'will you help me' in query or 'do you help me' in query:
            SpeakEngine.speak("of course? why not?")

        elif 'hi jarvis' in query or 'hello jarvis' in query or 'hey jarvis' in query or 'hay jarvis' in query or 'oy jarvis' in query:
            SpeakEngine.speak("Hello Sir, How may i help you?")
        
        elif 'how are you' in query:
            SpeakEngine.speak("I am fine sir")
        
        elif 'what are you doing' in query:
            SpeakEngine.speak(" i am SpeakEngine.speaking with you")






        ### Fun with Jarvis

        elif 'jigo' in query or 'jignesh' in query or 'jigs' in query or 'jiga' in query:
            playsound("/home/vishal/Further Study/Further Study/Python Projects/Jarvis/venv/ghar.mp3")
        
        elif 'lagna' in query or 'lagan' in query or 'lagn' in query or 'are you married' in query:
            playsound("/home/vishal/Further Study/Further Study/Python Projects/Jarvis/venv/ghar.mp3")
        
        elif 'tumhari koi girlfriend hai' in query or 'tumhari koi girlfriend hey' in query:
                playsound("/home/vishal/Further Study/Further Study/Python Projects/Jarvis/venv/ghar.mp3")
        






       
        ### Wikipedia Search

        elif 'wikipedia' in query:
            SpeakEngine.speak("Searching Wikipedia...")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query, sentences = 3)
            SpeakEngine.speak("According to wikipedia")
            print(result)
            SpeakEngine.speak(result)
        




        ### Open Some websites

        ### for open YouTube
        elif 'open youtube' in query or 'open the youtube' in query:
            SpeakEngine.speak("Ok Sir")
            webbrowser.open("youtube.com")

        
        ### For open Google
        elif 'open google' in query or 'open the google' in query:
            SpeakEngine.speak("Ok Sir")
            webbrowser.open("google.com")


        ### For Open Facebook
        elif 'open facebook' in query or 'open the facebook' in query:
            SpeakEngine.speak("Ok Sir")
            webbrowser.open("facebook.com")


        ### For open Instagram
        elif 'open instagram' in query or 'open the instagram' in query or 'open insta' in query or 'open the insta' in query:
            SpeakEngine.speak("Ok Sir")
            webbrowser.open("instagram.com")


        ### For open StackOverFlow
        elif 'open stack overflow' in query or 'open stackoverflow' in query:
            SpeakEngine.speak("Ok Sir")
            webbrowser.open("stackoverflow.com")


        ### For open Quora
        elif 'open quora' in query or 'jarvis open quora' in query:
            SpeakEngine.speak("Ok Sir")
            webbrowser.open("quora.com")






        elif 'play music' in query or "play the music" in query or "play song" in query:
            SpeakEngine.speak("Ok Sir")
            playSpotify()
            # music_dir = '/home/vishal/Entertainment/Music/MP3/holl'
            # songs = os.listdir(music_dir)
            # filepath = os.path.join(music_dir,songs[0])
            # print(filepath)
            





        ### amazing Functionality
            
        ### what is time

        elif 'the time' in query or 'what is time' in query:
            time = datetime.datetime.now().strftime("%H Hours and %M Minutes")
            print(time)
            SpeakEngine.speak("Sir the time is ")
            SpeakEngine.speak(time)

        
        ### send mail nut not working

        elif 'sent email' in query or 'send email' in query or 'sent mail' in query or 'send mail' in query:
            SpeakEngine.speak("To whom, do you want to send the email?")
            email = takeCommand()
            sendmail(email)
        

        ### play spotify music but not working

        elif 'play music on spotify' in query or 'play spotify' in query:
            playSpotify()



        ### for meaning of any word or vocabulary
        elif 'tell me the meaning of' in query or 'tell me meaning of' in query or 'what is the meaning of' in query or 'what is meaning of' in query or 'give me meaning of' in query or 'say me the meaning of' in query or 'say me meaning of' in query:
            result = query.split("meaning of ")
            result = result[1].split(" ")[0]
            res = "Ok sir, The Meaning of " + result + "is "
            temp = Dictionary.meaning(result)
            if temp == "Sorry sir, Not Found":
                speak(temp)
            else:
                SpeakEngine.speak("Ok Sir, The Meaning of ")
                SpeakEngine.speak(result)
                SpeakEngine.speak("is")
                SpeakEngine.speak(temp)
 
        
        else:
            print(query)
