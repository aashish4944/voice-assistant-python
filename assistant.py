import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import pyjokes
from MyAlarm import alarm

engine = pyttsx3.init()


def speak(text):
    engine.say(text)
    print(text)
    engine.runAndWait()


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        query = r.recognize_google(audio, language='en-in')
        print("You said:", query)
        return query.lower()
    except Exception as e:
        print("Error:", e)
        speak("Say that again")
        return ""


def runAssistant():
    speak("Assistant started")

    while True:
        query = takecommand()

        if "start" in query:
            speak("Hello how are you?")

        elif "time" in query:
            t = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Time is {t}")

        elif "open google" in query:
            webbrowser.open("https://google.com")

        elif "funny" in query:
            speak(pyjokes.get_joke())

        elif "set alarm" in query or "alarm" in query:
            speak("What time should I set the alarm? Please say like 9:50 PM")
            timing = takecommand()
            speak(f"Setting alarm for {timing}")
            alarm(timing)

        elif "exit" in query:
            speak("Goodbye")
            break


if __name__ == "__main__":
    runAssistant()