import speech_recognition as sr
from sre_constants import SUCCESS
import numpy as np
import os
import time
import pyttsx3
import webbrowser
import time
import cv2
r = sr.Recognizer()



def Kakku(matn):
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    volume = engine.getProperty('volume')
    voices = engine.getProperty('voices') 
    engine.setProperty('rate', 200)
    engine.setProperty('volume',1.0)
    engine.setProperty('voice', voices[0].id)
    engine.say(matn)
    engine.runAndWait()
    engine.stop()



call=['komarock','rock','amrock','what up','omura','amara','manga rock','rainbow rock','iraq','bungalow','bulldog']

user={
    "ism_sharif":"Komiljon",
    "raqam":"934057200",
    #"surat": cv2.imread("audio/dadam.jpg")           

}


def record_audio(ask = False):
    with sr.Microphone() as source:
     if ask:
        print(ask)
     audio = r.listen(source)
    voice_data = ''
    try:
     voice_data = r.recognize_google(audio)
     print(voice_data)
    except sr.UnknownValueError:
        Kakku("I am sorry, I do not understand you :(")
    except sr.RequestError:
        Kakku("I am sorry, I can not hear without internet :(")
    return voice_data

def respond(voice_data):
    if "what is your name" in voice_data:
        Kakku(f'My name is Kakku!')
    elif "Telegram" in voice_data:
        Kakku(f'Opening  {voice_data}')
        os.startfile(r'D:/мултик/Telegram Desktop/Telegram.exe')
    elif "word" in voice_data:
        Kakku(f'Opening  {voice_data}')
        os.startfile(r'"C:/Program Files/Microsoft Office/root/Office16\WINWORD.EXE"')
    elif "Google" in voice_data:
        Kakku(f'Opening  {voice_data}')
        os.startfile(r'"C:/Program Files/Google/Chrome\Application/chrome.exe"')
    elif "time" in voice_data:
        Kakku(f'Current time is {time.ctime()}')
    elif "search" in voice_data:
        search = record_audio("Nima qidirishimiz kerak?")
        url = 'https://google.com/search?q='+search
        webbrowser.get().open(url)
        Kakku(f'Here what I found for {search}')
    elif "find location" in voice_data:
        location = record_audio("Qayerni qidirishimiz kerak?")
        url = 'https://google.nl/maps/place/'+location+'/&amp;'
        webbrowser.get().open(url)
        Kakku(f'Here is your  {location}')
        
    elif voice_data.lower() == "video":
        capture=cv2.VideoCapture(1)
        capture.set(3,3840) #defines width
        capture.set(4,600)
        capture.set(10,300)
        while True:
             SUCCESS, img=capture.read()
             cv2.imshow("Video",img)
             if cv2.waitKey(1) & 0xFF == ord('k'):
                break
         
    elif voice_data.lower() in call:
        print("Qo'ng'iroq")

    elif voice_data.lower() == "father":
        imgResize = cv2.resize(user['surat'],(400,320))
        cv2.imshow(f'{user["ism_sharif"]} \n {user["raqam"]} ',imgResize)
        cv2.waitKey(0)

    elif 'exit' in voice_data:
        exit()

Kakku("How can I help you?")
voice_data = record_audio()
respond(voice_data)