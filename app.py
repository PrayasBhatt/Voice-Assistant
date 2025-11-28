import pyttsx3
import speech_recognition as sr

# Text to Speech  
engine = pyttsx3.init()
engine.setProperty('rate',150)
engine.setProperty('volume',1.0)

def speak(text):
    print("Assistant: ", text)
    engine.say(text)
    engine.runAndWait()

# Speech to Text
