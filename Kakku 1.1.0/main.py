from msilib.schema import AppId
import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget

import speech_recognition as sr
from sre_constants import SUCCESS
import numpy as np
import os
import time
import pyttsx3
import webbrowser
import time


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
    elif 'exit' in voice_data:
        exit()



class Yordamchi(Widget):

    def start(self):
        time.sleep(1)
        Kakku("How can I help you?")
        while 1:
            voice_data = record_audio()
            respond(voice_data)

    def cancel(self):
        App.get_running_app().stop()


class Asosiy(App):
    def build(self):
        return Yordamchi()

if __name__ == '__main__':
    Asosiy().run()
    