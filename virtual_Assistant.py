import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

e= pyttsx3.init('sapi5')
voices= e.getProperty('voices')
e.setProperty('voice',voices[0].id)


def speak(audio): 
    e.say(audio)
    e.runAndWait()
def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("GOOD MORNING!")
    elif hour>=12 and hour<18:
        speak("GOOD AFTERNOON!")
    else:
        speak("GOOD EVENING!")
    speak("i am jarvis sir please tell  me how may i help you")
    
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio=r.listen(source)
        
        
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')
        print(f"user said:{query}\n")    
        
    except Exception as e:
       
        print("say that again please....")
        return "none"
    return query
if __name__ == "__main__":
    wishme()
    while True:
    #if  1:
            
     query=takeCommand().lower()
     if 'wikipedia' in query:
         speak("searching wikipedia....")
         query=query.replace("wikipedia","")
         r=wikipedia.summary(query, sentences=1000000)          
         speak("ACCORDING TO WIKIPEDIA")
         print(r)
         speak(r)
     elif 'open youtube' in query:
         speak("opening youtube sir")
         webbrowser.open("youtube.com")
     elif 'open google' in query:
         webbrowser.open("google.com")
     elif 'open udemy' in query:
         speak("opening udemy sir")
         webbrowser.open("udemy.com")
     elif 'open stackoverflow' in query:
         webbrowser.open("stackoverflow.com")
     elif 'open hotstar' in query:
         speak("opening hotstar sir")
         webbrowser.open("hotstar.com")
     elif 'open whatsapp' in query:
         webbrowser.open("whatsapp web.com")
     elif 'open edge' in query:
         webbrowser.open("microsoft edge.com")
     elif 'open ff' in query:
         webbrowser.open("pornhub.com")
         speak("opening porn hub pandago")
     elif "the time" in query:
         strTime=datetime.datetime.now().strftime("%H:%M:%S")
         speak(f"sir the time is {strTime}") 
     elif 'open zoom' in query:
         codepath="C:\\Users\\rosha\AppData\\Roaming\\Zoom\\bin\\Zoom.exe"
         speak("opening zoom sir")
         os.startfile(codepath)
     elif 'open type king' in query:
         codepath ="D:\\TypingMaster11\\TypingMaster.exe"
         os.startfile(codepath)
     elif "open code" in query:
         codepath="C:\\Users\\rosha\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
         speak("opening code sir")
         os.startfile(codepath)
     elif 'open video' in query:
         codepath="C:\\Program Files\\VideoLAN\VLC\\vlc.exe"
         os.startfile(codepath)
     elif 'open free fire' in query:
         codepath="C:\\Program Files\\BlueStacks_nxt\\HD-Player.exe"
         speak("opening free fire sir")
         os.startfile(codepath)
    