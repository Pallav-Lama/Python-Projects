import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# def sendEmail(to, content):
#     server = smtplib.SMTP("smtp.gmail.com", 587)
#     server.ehlo()
#     server.starttls()
#     server.login("pallavlama9@gmail.com", "password")
#     server.sendmail("pallavlama9@gmail.com", to, content)
#     server.close

def wishMe():
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 17:
        speak("Good Afternoon!")
    elif hour >= 17 and hour < 21:
        speak("Good Evening!")
    else: 
        speak("Good Night!")
    
    speak("I am Jarvis, your personal virtual assistant. How can I help you?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.energy_threshold = 400
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language= 'en-in')
        print(f"User said: {query} \n")
    except Exception as e:
        # print(e)
        print("I could not get you. Could you please repeat that again")
        return "None"
    return query
if __name__ == "__main__":
    # speak("My name is Pallav Lama.")
    wishMe()
    while True:
        query = takeCommand().lower()

        #logic for executing tasks based on query
        if "wikipedia" in query:
            speak("searching wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif "open youtube" in query:
            speak("opening youtube...")
            webbrowser.open("youtube.com")

        elif "open facebook" in query:
            speak("opening facebook...")
            webbrowser.open("facebook.com")
        
        # elif "open google" in query:
        #     speak("opeing google...")
        #     webbrowser.open("google.com")
        
        elif "play music" in query:
            speak("Playing mucic...")
            music_dir = "C:\\Users\\admin\\Desktop\\English Songs"
            songs = os.listdir(music_dir)
            # print(songs)
            i = random.randint(0, len(songs) - 1)
            # print(i)
            os.startfile(os.path.join(music_dir, songs[i]))
        
        elif "open google chrome" in query:
            speak("Opening google chrome....")
            codePath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(os.path.join(codePath))

        elif "time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The current time is {strTime}")

        # elif "email to pallav" in query:
        #     try:
        #         speak("What should I write?")
        #         content = takeCommand()
        #         to = "pallavlama9@gmail.com"
        #         sendEmail(to, content)
        #         speak("Email has been sent")

        #     except Exception as e:
        #         print(e)
        #         speak("Sorry I was enable to send email")

        elif "quit" in query:
            speak("Thanks for using me.")
            exit()
