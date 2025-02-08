import os
import random
import sys
import subprocess
import webbrowser
import requests
import json
import pyttsx3
import speech_recognition as sr
import urllib.request
import re
from datetime import datetime, timedelta
import schedule
from dotenv import load_dotenv  # Import dotenv to load environment variables

# Load environment variables from .env file
load_dotenv()

class VoiceAssistant:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.engine = pyttsx3.init()
        self.engine.setProperty("rate", 150)
        self.engine.setProperty("voice", self.engine.getProperty("voices")[0].id)
        
        # Fetch API keys from environment variables
        self.weather_api_key = os.getenv("WEATHER_API_KEY")  # Get from .env file
        self.news_api_key = os.getenv("NEWS_API_KEY")  # Get from .env file
        self.is_speaking = False

    def speak(self, text):
        """Speak the given text."""
        if not self.is_speaking:
            self.is_speaking = True
            self.engine.say(text)
            self.engine.runAndWait()
            self.is_speaking = False

    def listen_and_respond(self):
        """Listen for a command from the user."""
        try:
            with sr.Microphone() as source:
                print("Adjusting for ambient noise...")
                self.recognizer.adjust_for_ambient_noise(source)
                print("Listening...")
                audio = self.recognizer.listen(source)
            return self.recognizer.recognize_google(audio).lower()
        except sr.UnknownValueError:
            return "Sorry, I couldn't understand that."
        except sr.RequestError as e:
            return f"Request error: {e}"
        except Exception as e:
            return f"An error occurred: {e}"

    def process_command(self, command, skip_news=False):
        """Process the given command and return the appropriate response."""
        if "news" in command.lower():
            if skip_news:
                return "Skipping news headlines."
            return self.get_news()
        elif "weather" in command.lower():
            city = command.replace("weather in", "").strip()
            return self.get_weather(city)
        elif "play" in command.lower() and "youtube" in command.lower():
            video_title = command.lower().replace("play", "").replace("on youtube", "").strip()
            if video_title:
                return self.play_youtube(video_title)
            else:
                return "Please specify a video title to play in YouTube."
        elif "search for" in command.lower():
            file_name = command.lower().replace("search for", "").strip()
            if file_name:
                return self.search_file(file_name)
            else:
                return "Please specify the file name to search for."
        elif "play local music" in command.lower():
            return self.play_local_music()
        elif "joke" in command.lower():
            return self.get_joke()
        elif "help" in command.lower():
            return self.get_help()
        elif "goodbye" in command.lower():
            self.speak("Goodbye! Exiting now.")
            sys.exit()
        elif "open" in command.lower():
            website = command.lower().replace("open","").strip()
            return self.open_website(website)
        elif "best college in india" in command.lower():
            return "India has many top colleges, but IIT Madras and IIT Kharagpur stand out as top colleges"
        elif "best college in telangana" in command.lower():
            return "Oh, that's easy! IARE is not just the best in Telangana, it's probably the only place where students are more punctual and disciplined!"
        elif "terminate" in command.lower() or "shut down" in command.lower():
            self.speak("Shutting down. Goodbye!")
            sys.exit()
        elif "deactivate" in command.lower():
            self.speak("Deactivating voice assistant. Waiting for activation.")
            return "Voice assistant deactivated."

        else:
            return "Sorry, I can't perform that task."

    def open_website(self, command):
        """Open a predefined or user-specified website."""
        predefined_sites = {
            "youtube": "https://www.youtube.com",
            "google": "https://www.google.com",
            "gmail": "https://www.gmail.com",
            "spotify": "https://open.spotify.com",
            "iare": "https://iare.ac.in/",
            "iari": "https://iare.ac.in/",
        }
        for site, url in predefined_sites.items():
            if site in command:
                webbrowser.open(url)
                return f"Opening {site}."
        try:
            site_name = command.replace("open", "").strip()
            webbrowser.open(f"https://{site_name}.com")
            return f"Opening {site_name}."
        except Exception:
            return "Website not recognized."

    def search_file(self, file_name):
        """Search for a file in the user's directory."""
        search_path = os.path.expanduser("~/")  # Start from the user's home directory
        for root, dirs, files in os.walk(search_path):
            if file_name.lower() in (file.lower() for file in files):
                file_path = os.path.join(root, file_name)
                print("File found: {file_path}")
                return f"File found: {file_path}"
        return f"File '{file_name}' not found."
    
    def open_folder(self, file_name):
        """Open the folder containing the specified file."""
        search_path = os.path.expanduser("~/")  # Start from the user's home directory
        for root, dirs, files in os.walk(search_path):
            if file_name.lower() in (file.lower() for file in files):
                folder_path = root
                try:
                    subprocess.Popen(f'explorer "{folder_path}"' if os.name == 'nt' else ['xdg-open', folder_path])
                    return f"Opened folder containing '{file_name}'."
                except Exception as e:
                    return f"Could not open folder: {e}"
        return f"File '{file_name}' not found."

    def play_local_music(self):
        """Play a random song from the Music folder."""
        try:
            folder_path = os.path.expanduser("~/Music")  # Explicit path to Music folder
            if not os.path.exists(folder_path):
                return "The Music folder does not exist."

            music_files = [file for file in os.listdir(folder_path) if file.endswith(('.mp3', '.wav'))]
            if not music_files:
                return "No music files found in the Music folder."

            song_to_play = random.choice(music_files)
            song_path = os.path.join(folder_path, song_to_play)
            os.startfile(song_path)  # For Windows
            return f"Now playing: {song_to_play}"
        except Exception as e:
            return f"An error occurred while playing music: {e}"

    def get_weather(self, city):
        """Fetch weather details for a given city."""
        base_url = "https://api.openweathermap.org/data/2.5/weather"
        try:
            response = requests.get(base_url, params={"q": city, "appid": self.weather_api_key})
            data = response.json()
            if data["cod"] == 200:
                temp = data["main"]["temp"] - 273.15  # Convert Kelvin to Celsius
                desc = data["weather"][0]["description"]
                humidity = data["main"]["humidity"]
                return f"The temperature in {city} is {temp:.1f}°C with {desc} and humidity at {humidity}%."
            return "City not found."
        except Exception as e:
            return f"Error fetching weather: {e}"

    def get_news(self):
        """Fetch the latest news headlines."""
        url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={self.news_api_key}"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                articles = response.json()["articles"][:5]
                headlines = [article["title"] for article in articles]
                return "Here are the latest headlines:\n" + "\n".join(headlines)
            return "Unable to fetch news."
        except Exception as e:
            return f"Error fetching news: {e}"

    def play_youtube(self, query):
        """Play a video on YouTube."""
        query = query.replace(" ", "+")
        try:
            html = urllib.request.urlopen(f"https://www.youtube.com/results?search_query={query}")
            video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
            if video_ids:
                webbrowser.open(f"https://www.youtube.com/watch?v={video_ids[0]}")
                return f"Playing {query.replace('+', ' ')} on YouTube."
            return "No videos found."
        except Exception as e:
            return f"Error playing YouTube video: {e}"

    def get_joke(self):
        """Fetch a random joke."""
        url = "https://v2.jokeapi.dev/joke/Any"
        try:
            response = requests.get(url)
            joke = response.json()
            if joke["type"] == "single":
                return joke["joke"]
            return f"{joke['setup']} ... {joke['delivery']}"
        except Exception as e:
            return f"Error fetching joke: {e}"

    def get_help(self):
        """Provide a list of available commands."""
        return (
            "Here are the commands you can use:\n"
            "1. Open [website name] - Opens a website.\n"
            "2. News - Fetches the latest news headlines.\n"
            "3. Weather in [city name] - Fetches the weather for a specific city.\n"
            "4. Play in YouTube [query] - Plays a video on YouTube.\n"
            "5. Joke - Tells a random joke.\n"
            "6. Help - Provides a list of commands.\n"
            "7. Goodbye - Exits the assistant."
        )

    def output_and_speak(self, text, update_ui_callback):
        """Output text to the UI and speak it."""
        update_ui_callback(text)  # Update the UI first
        self.speak(text)
