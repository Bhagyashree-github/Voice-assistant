# In this project i am making a personal virtual assistant 
# the modules used here are pyttsx : text to speech convert
# speech recognition: Library for performing speech recognition, with support for several engines and APIs, online and offline.
# datetime:
# wikipedia:
# webbrowser:
# os:
# smtplib:
 
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib 

def speak(content):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    engine.say(content)
    engine.runAndWait() 
speak('hi lucky ... i am ready to take commands...')

def wishme():
    dat = datetime.datetime.now().hour
    
    if dat > 12 and dat <18:
        speak('good afternoon...')
    elif dat>18 and dat <0:
        speak('good evening')
    elif dat >6 and dat < 12:
        speak('Good morning')
    elif dat == 12:
        speak('good noon')
    else:
        speak("it's time for sleep")

# wishme()

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('say something...')
        audio = r.listen(source)
    try :
        print('recognizing')
        query = r.recognize_google(audio,language = 'en-in')
        print(f'you said :{query}\n')

    except :
        print('Say taht again please')
        query = None
    return query
# takecommand()
# Logic for executing the task 
query = str(takecommand())
if 'wikipedia' in query.lower():
    speak('Searching wikipedia...')
    query = query.replace('wikipedia','') # i am removing wikipedia from the string to be searched bcz i don't want to search wikipedia inside wikipedia
    result = wikipedia.summary(query , sentences = 2)
    speak(result)
elif 'open youtube' in query.lower():
    speak('opening youtube...')
    url = 'youtube.com'
    chrome_path = 'C://Program Files (x86)//Google//Chrome//Application//chrome.exe %s'
    webbrowser.get(chrome_path).open(url)

elif 'open google' in query.lower():
    speak('opening google...')
    url = 'google.com'
    chrome_path = 'C://Program Files (x86)//Google//Chrome//Application//chrome.exe %s'
    webbrowser.get(chrome_path).open(url)

elif 'open geeksforgeeks' in query.lower():
    speak('opening google...')
    url = 'geeksforgeeks.com'
    chrome_path = 'C://Program Files (x86)//Google//Chrome//Application//chrome.exe %s'
    webbrowser.get(chrome_path).open(url)
elif 'play music' in query.lower():
    song_path = 'C:\\Users\\Bikram Sahoo\\music'
    songs= os.listdir(song_path)
    os.startfile(os.path.join(song_path,songs[0]))