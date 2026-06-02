import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary

recogniser = sr.Recognizer()
engine = pyttsx3.init()


def speak(text):
    engine.say(text)
    engine.runAndWait()


def processCommand(c):
    c = c.lower()

    if "open google" in c:
        webbrowser.open("https://google.com")

    elif "open youtube" in c:
        webbrowser.open("https://youtube.com")

    elif "open linkedin" in c:
        webbrowser.open("https://linkedin.com")

    elif "open instagram" in c:
        webbrowser.open("https://instagram.com")

    elif c.startswith("play"):

        # remove "play"
        song = c.replace("play", "").strip()

        print("Song requested:", song)

        # check if song exists
        if song in musiclibrary.music:
            link = musiclibrary.music[song]
            speak(f"Playing {song}")
            webbrowser.open(link)

        else:
            speak("Song not found")
            print("Available songs:", musiclibrary.music.keys())


if __name__ == "__main__":

    speak("Initializing Jarvis")

    while True:

        try:
            with sr.Microphone() as source:

                print("Listening for wake word...")
                audio = recogniser.listen(source)

                word = recogniser.recognize_google(audio)

                print("Heard:", word)

                if "jarvis" in word.lower():

                    speak("Yes")

                    with sr.Microphone() as source:

                        print("Jarvis Active...")
                        audio = recogniser.listen(source)

                        command = recogniser.recognize_google(audio)

                        print("Command:", command)

                        processCommand(command)

        except Exception as e:
            print("Error:", e)