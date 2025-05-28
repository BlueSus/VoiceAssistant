import os
import requests
from speech_utils import speak
from datetime import datetime

def get_time():
    now = datetime.now()
    current_time = now.strftime("%I:%M %p")
    speak(f"The current time is {current_time}")
def get_weather(city):
    API_KEY = os.getenv("WEATHERAPI_KEY")
    if not API_KEY:
        speak("Weather API key is missing.")
        return
    try:
        url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}&aqi=no"
        response = requests.get(url)
        data = response.json()
        if "error" not in data:
            location = data['location']['name']
            region = data['location']['region']
            country = data['location']['country']
            temp_f = data['current']['temp_f']
            feelslike_f = data['current']['feelslike_f']
            condition = data['current']['condition']['text']
            message = (
                f"The current weather in {location}, {region}, {country} is {condition}. "
                f"It is {temp_f}°F and feels like {feelslike_f}°F."
            )
            speak(message)
        else:
            speak(f"City '{city}' not found. Please try again.")
    except Exception as e:
        speak(f"Error fetching weather: {e}")
