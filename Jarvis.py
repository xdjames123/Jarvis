import openai
import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random 
from datetime import datetime
import requests
import re
import time
import shutil
import subprocess 
import math
import pyaudio


engine = pyttsx3.init()
engine.setProperty('rate', 180)
engine.runAndWait()

engine.setProperty('volume', 1.0)  

websites = {
    "google": "https://www.google.com",
    "youtube": "https://www.youtube.com",
    "facebook": "https://www.facebook.com",
    "instagram": "https://www.instagram.com",
    "twitter": "https://www.twitter.com",
    "wikipedia": "https://www.wikipedia.org",
    "amazon": "https://www.amazon.com",
    "reddit": "https://www.reddit.com",
    "linkedin": "https://www.linkedin.com",
    "tiktok": "https://www.tiktok.com",
    "pinterest": "https://www.pinterest.com",
    "netflix": "https://www.netflix.com",
    "ebay": "https://www.ebay.com",
    "yahoo": "https://www.yahoo.com",
    "whatsapp": "https://www.whatsapp.com",
    "spotify": "https://www.spotify.com",
    "github": "https://www.github.com",
    "dropbox": "https://www.dropbox.com",
    "quora": "https://www.quora.com",
    "zoom": "https://www.zoom.us",
    "microsoft": "https://www.microsoft.com",
    "apple": "https://www.apple.com",
    "adobe": "https://www.adobe.com",
    "etsy": "https://www.etsy.com",
    "wordpress": "https://www.wordpress.com",
    "stackoverflow": "https://www.stackoverflow.com",
    "bbc": "https://www.bbc.com",
    "cnn": "https://www.cnn.com",
    "airbnb": "https://www.airbnb.com",
    "shopify": "https://www.shopify.com",
    "google": "https://www.google.com"
}

def speak(text):
    """Converts text to speech and also prints it to the terminal."""
    print(f"J.A.R.V.I.S: {text}") 
    engine.say(text) 
    engine.runAndWait() 


def listen():
    recognizer = sr.Recognizer()
    
    try:
        print("Initializing microphone...")
        with sr.Microphone() as source:
            
            print("Calibrating microphone to ambient noise...")
            recognizer.adjust_for_ambient_noise(source, duration=2)
            
            print("Listening for command...")
            audio = recognizer.listen(source)
            
            # Recognize the speech using Google's API
            command = recognizer.recognize_google(audio)
            print(f"Recognized Command: {command}")
            return command.lower()
    
    except sr.UnknownValueError:
        print("Could not understand audio")
        return None
    except sr.RequestError as e:
        print(f"Request Error from Google Speech Recognition: {e}")
        return None
    except OSError as e:
        print(f"Microphone Error: {e}")
        return None

def open_website(site_name):
    """Opens a website."""
    websites = {
        "google": "https://www.google.com",
        "youtube": "https://www.youtube.com",
        "instagram": "https://www.instagram.com",
        "reddit": "https://www.reddit.com",
        "facebook": "https://www.facebook.com"
    }
    if site_name in websites:
        speak(f"Very well, opening {site_name} for you, sir.")
        webbrowser.open(websites[site_name])
    else:
        speak("Website not found in my database, sir.")


def search_wikipedia(query):
    """Searches Wikipedia and returns a summary."""
    try:
        summary = wikipedia.summary(query, sentences=2)
        return summary
    except Exception as e:
        return "I couldn't find any relevant information, sir."

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Function to speak text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to listen for music type (relaxing, focus, chill, or motivation)
def listen_for_music_type():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        speak("Listening for your music type...")  # Ask the user to speak
        print("Listening for your response...")  # For debugging in terminal
        try:
            audio = recognizer.listen(source)  # Listen to the user
            response = recognizer.recognize_google(audio)  # Recognize the speech
            print(f"User said: {response}")  # Debug print
            return response.lower()  # Return the response in lowercase
        except sr.UnknownValueError:
            speak("Sorry, I couldn't understand that. Please try again.")
            return ""  # Return empty string if not recognized
        except sr.RequestError:
            speak("Sorry, there was an error with the speech service.")
            return ""  # Return empty string if there was a request error

# Main function to play music based on the user's command8
def play_music(command):
    command = command.lower()  # Convert command to lowercase to make it case-insensitive

    if "play music" in command:  # Check if "play music" is in the command
        speak("What kind of music would you like to hear? Relaxing, focus, chill, or motivational?")
        user_response = listen_for_music_type()  # Wait for the user's response

        if "relaxing" in user_response:
            url = "https://www.youtube.com/watch?v=WmJHD5jJj2w&t=136s"
            webbrowser.open(url)
            speak("Playing relaxing music, sir.")
        elif "focus" in user_response:
            url = "https://www.youtube.com/watch?v=FxJ3zPUU6Y4&t=550s"
            webbrowser.open(url)
            speak("Playing focus music, sir.")
        elif "chill" in user_response:
            url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"  # Placeholder URL for Chill Music
            webbrowser.open(url)
            speak("Playing chill music, sir.")
        elif "motivation" in user_response:
            url = "https://www.youtube.com/watch?v=9iUJ8kOCfKM"  # Placeholder URL for Motivation Music
            webbrowser.open(url)
            speak("Playing motivational music, sir.")
        else:
               speak("Sorry, I didn't understand that. Please say relaxing, focus, chill, or motivation.")
    else:
        speak("Sorry, I didn't understand your music request, sir.")

def process_math_command(command):
    command = command.lower()
    if "x" in command or "*" in command:
        # Solve multiplication
        numbers = [int(s) for s in command.split() if s.isdigit()]
        if len(numbers) == 2:
            result = numbers[0] * numbers[1]
            speak(f"The result is {result}, sir.")
        else:
            speak("Invalid multiplication command, sir.")
    elif "sin" in command:
        # Solve sine operation
        import math
        num = float(command.split()[1])
        result = math.sin(math.radians(num))
        speak(f"The result of sin({num}) is {result}, sir.")
    else:
        speak("My apologies, sir. It appears your request has me momentarily stumped.")


def solve_math_problem(query):
    """Solve math problems with J.A.R.V.I.S.'s precise tone."""
    try:
        query = re.sub(r'\b(what is |)')
        query = re.sub(r'\b(what is|calculate|solve|please)\b', '', query)
        query = re.sub(r'\b(into|times|x)\b', '*', query)
        result = eval(query.strip())
        speak(f"According to my calculations, the result is {result}, sir.")
    except Exception:
        speak("Apologies, Captain. I wasn't able to solve that problem, sir.")

def current_time():
    """Returns the current time."""
    now = datetime.now()
    return now.strftime("%H:%M:%S")

def get_weather(location):
    api_key = 'f939dffd7cead4fefaa81d4f7a9735d6'
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
    
    # Sending request to API
    response = requests.get(url)
    
    # Check if the response is a 404 error (City not found)
    if response.status_code == 404:
        return f"Sorry, the city '{location}' could not be found, sir. Please try again with a valid city name."
    
    # If the request was successful (status code 200)
    if response.status_code == 200:
        data = response.json()
        city = data["name"]
        country = data["sys"]["country"]
        temp = data["main"]["temp"]
        weather_description = data["weather"][0]["description"]
        return f"The current weather in {city}, {country} is {temp}°C with {weather_description}, sir."
    
    return "Sorry, I couldn't fetch the weather information for that location, sir."

def process_command(command):
    command = command.lower()

    if "what is the weather" in command:
        # Extract location from the command, removing "what is the weather" and "in"
        location = command.replace("what is the weather", "").replace("in", "").strip()
        
        if location:  # If location is specified, fetch weather
            print(f"Location detected: {location}")  # Debug line to check extracted location
            weather_info = get_weather(location)
            speak(weather_info)  # Speak the weather info and print it
        else:  # If no location is specified, prompt the user
            speak("It seems I couldn't catch the location, sir. Could you please specify the city?")
    
    
    elif "time" in command:
        speak(f"The time is precisely {current_time()}, sir. Always punctual.")
    
    elif "open" in command and any(site in command for site in websites.keys()):
        site = command.replace("open", "").strip()
        open_website(site)
    
    elif "play music" in command:
        play_music(command)
    
    elif "tell me about" in command or "who is" in command:
        topic = command.replace("tell me about", "").replace("who is", "").strip()
        speak(search_wikipedia(topic))
    
    elif "sin" in command or "x" in command or "*" in command:
        solve_math_problem(command)
    
    elif any(word in command for word in ["exit", "quit", "shutdown"]):  # Fixed condition
        speak("As you wish, sir. Shutting down.")
        exit()
    
    else:
        speak("My apologies, sir. It appears your request has me momentarily stumped.")

def main():
    """Main function for Jarvis."""
    speak("Hello, I am Jarvis, your personal assistant. How can I assist you, sir?")
    while True:
        command = listen()
        if command:
            process_command(command)

if __name__ == "__main__":
    main()