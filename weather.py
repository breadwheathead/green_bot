import requests
from config import OPEN_WEATHER_API_KEY

URL = f'https://api.openweathermap.org/data/3.0/onecall?' \
      f'lat={lat}&lon={lon}&exclude=current&appid={OPEN_WEATHER_API_KEY}&units=metric&land=ru'

def get_weather(city):
    try:
        r = requests.get()