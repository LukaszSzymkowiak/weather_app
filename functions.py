import requests
import os
from dotenv import load_dotenv


def get_url():
    load_dotenv()
    return os.getenv("WEATHER_URL")


def get_api_key():
    load_dotenv()
    return os.getenv("API_KEY")


def get_weather(url, city, api_key):
    return requests.get(
        f"{url}{city}&appid={api_key}&units=metric").json()


def view_weather():
    weather_url = get_url()
    api_key = get_api_key()
    degree_sign = u"\N{DEGREE SIGN}"
    city_input = input("Enter city or 'q' to quit: ").lower()
    if city_input == "q":
        print("Closed.")
        exit()
    else:
        weather_data = get_weather(weather_url, city_input, api_key)
        print(f"\nCity: {weather_data['name']}\n"
              f"Country: {weather_data['sys']['country']}\n"
              f"Temperature: {weather_data['main']['temp']} {degree_sign}C\n"
              f"Feels like: {weather_data['main']['feels_like']} {degree_sign}C\n")
