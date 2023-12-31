import speech_recognition as sr
import pyttsx3
import webbrowser
import subprocess
from datetime import datetime
import os
import pygame

def play_music():
    music_path = "C:/Users/MONSTER/Desktop/music/müslüm.mp3"  # Değiştirilmesi gereken dosya yolu
    try:
        speak("Playing music müslüm.")
        os.system(f"start {music_path}")
    except Exception as e:
        speak(f"Sorry, I encountered an error while playing music: {e}")

def stop_music():
    try:
        speak("Stopping music.")
        os.system("taskkill /f /im vlc.exe")  # Eğer VLC kullanıyorsanız, uygun medya oynatıcıyı belirtin
    except Exception as e:
        speak(f"Sorry, I encountered an error while stopping music: {e}")

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio)
        print(f"You said: {query}")
        return query
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand the audio.")
        return None
    except sr.RequestError as e:
        print(f"Error making the request to Google Speech Recognition service; {e}")
        return None

def open_google():
    webbrowser.open("https://www.google.com")

def open_youtube():
    webbrowser.open("https://www.youtube.com")

def open_youtube_video(video_query):
    search_url = f"https://www.youtube.com/results?search_query={video_query}"
    webbrowser.open(search_url)

def open_application(application_name):
    try:
        subprocess.Popen(application_name, shell=True)
        speak(f"Opening {application_name}.")
    except Exception as e:
        speak(f"Sorry, I encountered an error while opening {application_name}: {e}")

def shutdown_computer():
    speak("Are you sure you want to shut down the computer? Say 'yes' to confirm.")
    response = listen()
    if response and "yes" in response.lower():
        speak("Shutting down the computer.")
        subprocess.Popen(["shutdown", "/s", "/t", "1"])

def play_jarvis():
    pygame.init()
    pygame.mixer.music.load("C:/Users/MONSTER/Desktop/jarvis asistant/jarvıs.mp3")
    pygame.mixer.music.set_volume(1.0)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

def main():
    play_jarvis()
    
    while True:
        query = listen()

        if query:
            if "hello" in query.lower():
                speak("Hi there!")

            elif "play music" in query.lower():
                play_music()

            elif "stop music" in query.lower():
                stop_music()    

            elif "closed system" in query.lower():
                speak("closing systems")
                break

            elif "open system" in query.lower():
                playsound("jarvıs.mp3")

            elif "open google" in query.lower():
                speak("Opening Google.")
                open_google()

            elif "open youtube" in query.lower():
                speak("Opening YouTube.")
                open_youtube()

            elif "open video from youtube" in query.lower():
                speak("Sure, what video would you like to watch?")
                video_query = listen()
                if video_query:
                    speak(f"Searching for {video_query} on YouTube.")
                    open_youtube_video(video_query)

            elif "open app" in query.lower():
                speak("Sure, which application would you like to open?")
                app_name = listen()
                if app_name:
                    open_application(app_name)

            elif "shut down" in query.lower():
                shutdown_computer()

            elif"what time"in query.lower():
                speak(f"The current time is {datetime.now().strftime('%H:%M')}.")

            elif "play music" in query.lower():
                play_music()

            else:
                speak("I'm sorry, I didn't understand that.")

if __name__ == "__main__":
    main()
