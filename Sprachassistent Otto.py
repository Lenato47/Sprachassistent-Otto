from gtts import gTTS
import speech_recognition as sr
import playsound
import wikipediaapi
import datetime
from selenium import webdriver
import time
import pyautogui
from selenium.webdriver.common.keys import Keys
import pyttsx3
import os
from bs4 import BeautifulSoup
import requests
import subprocess




engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice','voices[0].id')

def speakde(text):
    tts = gTTS(text=text, lang="de")
    filename = "Voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    os.remove("Voice.mp3")

def speaken(text):
    tts = gTTS(text=text, lang="en")
    filename = "Voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    os.remove("Voice.mp3")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio=r.listen(source)

        try:
            statement=r.recognize_google(audio,language='de')
            print(f"user said:{statement}\n")

        except Exception as e:
            return "None"
        return statement


def Erinnern():
    speakde("Woran soll ich dich erinnern?")
    reminder = takeCommand().lower()
    thisdict = {"einer": "1", "zwei": "2", "drei": "3", "vier": "4", "fünf": "5", "sechs": "6", "sieben": "7", "acht": "8","neun": "9"}
    if reminder != "":
        speakde("Wann? ")
        zeit = takeCommand().lower()
        if zeit != "":
                if "sekunde" in zeit:
                    zeit = zeit.replace("in","",1).replace("Sekunden","").replace("sekunden","").replace("Sekunde","").replace("sekunde","").replace("einer","1").replace("zwei","2").replace("drei","3").replace("vier","4").replace("fünf","5").replace("sechs","6").replace("sieben","7").replace("acht","8").replace("neun","9").replace(" ","")
                    zeit1 = int(zeit)
                    time.sleep(int(zeit1))
                    print("Hier ist deine Erinnerung an " + str(reminder))
                    speakde("Hier ist deine Erinnerung an " + str(reminder))
                elif "minute" in zeit:
                    zeit = zeit.replace("in","",1).replace("Minuten","").replace("minuten","").replace("Minute","").replace("minute","").replace("einer","1").replace("zwei","2").replace("drei","3").replace("vier","4").replace("fünf","5").replace("sechs","6").replace("sieben","7").replace("acht","8").replace("neun","9").replace(" ","")
                    zeit1 = int(zeit)*60
                    time.sleep(int(zeit1))
                    speakde("Hier ist deine Erinnerung an " + str(reminder))
                    print("Hier ist deine Erinnerung an " + str(reminder))
                elif "stunde" in zeit:
                    zeit = zeit.replace("in","",1).replace("Stunden","").replace("stunden","").replace("Stunde","").replace("stunde","").replace("einer","1").replace("zwei","2").replace("drei","3").replace("vier","4").replace("fünf","5").replace("sechs","6").replace("sieben","7").replace("acht","8").replace("neun","9").replace(" ","")
                    zeit1 = int(zeit)*3600
                    time.sleep(int(zeit1))
                    speakde("Hier ist deine Erinnerung an " + str(reminder))
                    print("Hier ist deine Erinnerung an " + str(reminder))

def GoogleEarth():
    subprocess.Popen("C:\Program Files\Google\Google Earth Pro\client\googleearth.exe")

def Program():
    subprocess.Popen("") #Dateipfad hier einfügen

def Uhrzeit():
    hour=datetime.datetime.now().hour
    minute = datetime.datetime.now().minute
    speakde("\"Es ist " + str(hour) + " Uhr " + str(minute) +"\"")

def Wikipedia():
    wiki_wiki = wikipediaapi.Wikipedia('de')
    speakde("Wonach soll gesucht werden? ")
    Wonach = takeCommand()
    results = wiki_wiki.page(str(Wonach)).summary
    if results == None:
        speakde("Entschuldigung, aber ich habe dich nicht verstanden")
    print(results)
    speakde(results)

def Nachrichten():
    source = requests.get("https://www.tagesschau.de/allemeldungen/").text
    soup = BeautifulSoup(source, "lxml")
    Nachrichten = (soup.find("div", class_="linklist withnolinkcontentbutnoproblem"))
    news = (Nachrichten.text).replace("Uhr", "").replace("-", "").replace("swr","").replace("mdr","")
    newslist = news.splitlines()
    counter = 2
    for i in range(20):
        speakde(newslist[counter])
        counter += 1
        if counter == 6:
            speakde("weitere Nachrichten?")
            statei = takeCommand().lower()
            if "ja" in statei:
                for i in range(5):
                    speakde(newslist[counter])
                    counter += 1


            else:
                break

def NSTAAF():
    driver = webdriver.Chrome()
    driver.get("https://www.google.com")
    pyautogui.click(700,820)
    time.sleep(1)
    driver.minimize_window()
    Folge = input("Welche Folge? : ")
    driver.maximize_window()
    Suche = driver.find_element_by_name("q")
    Suche.send_keys("no such thing as a fish " + str(Folge))
    Suche.send_keys(Keys.ENTER)
    time.sleep(1)
    driver.find_element_by_tag_name("cite").click()
    time.sleep(1)
    Länge = driver.find_element_by_class_name("total-time")
    Zahl = (Länge.text)
    Zahll = str(Zahl[:2])
    Schlafzahl = (int(Zahll)+1)*60
    driver.minimize_window()
    time.sleep(Schlafzahl)

def Wetter():
    source = requests.get("https://www.meteoblue.com/de/wetter/woche/wangerland_deutschland_3213143").text
    soup = BeautifulSoup(source, "lxml")
    Wetter = soup.find("div",class_="col-12 report no-top-padding").text
    speakde(Wetter)

def Youtube():
    driver = webdriver.Chrome()
    driver.get("https://www.youtube.com")

def Website():
    driver = webdriver.Chrome()
    driver.get("") #Website adresse hier einfügen

def Spotifystart():
    pyautogui.click(320, 1060) #Position des Spotify Icon in der taskbar hier anpassen
    time.sleep(3)
    pyautogui.press("space")
    pyautogui.click(320, 1060)

def Spotifynext():
    pyautogui.click(320, 1060)
    pyautogui.hotkey('ctrlleft', 'right')
    time.sleep(1)
    pyautogui.click(320, 1060)

def Spotifyquit():
    pyautogui.click(320, 1060)
    pyautogui.hotkey('ctrlleft', 'shiftleft', "q")

def Spotifylouder():
    pyautogui.click(320, 1060)
    pyautogui.hotkey('ctrlleft', 'up')
    time.sleep(1)
    pyautogui.click(320, 1060)

def Spotifyquieter():
    pyautogui.click(320, 1060)
    pyautogui.hotkey('ctrlleft', 'down')
    time.sleep(1)
    pyautogui.click(320, 1060)




while 1 != 0:
    statement = takeCommand().lower()
    if "otto" in statement:
        speaken("Ja?")
        for ii in range(1000):
            statement1 = takeCommand().lower()
            if "zeit" in statement1:
                Uhrzeit()
            elif "youtube" in statement1:
                Youtube()
            elif "erinnern" in statement1:
                Erinnern()
            elif "fisch" in statement1:
                NSTAAF()
            elif "wikipedia" in statement1:
                Wikipedia()
            elif "nachrichten" in statement1:
                Nachrichten()
            elif "wetter" in statement1:
                Wetter()
            elif "Program" in statement1:
                Program()
            elif "Website" in statement1:
                Website()
            elif "spotify" in statement1:
                Spotifystart()
                for iii in range(100):
                    statement2 = takeCommand().lower()
                    if "next" in statement2:
                        Spotifynext()
                    elif "lauter" in statement2:
                        Spotifylouder()
                    elif "leiser" in statement2:
                        Spotifyquieter()
                    elif "aus" in statement2:
                        Spotifyquit()
                        break
                    else:
                        continue
            elif "Stop" in statement1:
                quit()
            else:
                break
    else:
        continue
