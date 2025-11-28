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

r = sr.Recognizer()

def listen():
    with  sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Listening...")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print("User: ", text)
        return text.lower()
    except sr.UnknownValueError:
        return None
    except sr.RequestError as e:
        print("API error: ", e)
        return None

speak("Hello! How can I assist you today? Say 'exit' to quit.")

while True:
    command = listen()
    if command:
        if 'exit' in command:
            speak("Goodbye!")
            break
        else:
            speak(f"You said: {command}")
    else:
        speak("I didn't catch that. Could you please repeat?")