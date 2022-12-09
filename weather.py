import json
import datetime
import requests
from pprint import pprint
from config import OPEN_WEATHER_API_KEY

URL_CITY = 'http://api.openweathermap.org/geo/1.0/direct?q={}&&appid={}'
URL = 'http://api.openweathermap.org/data/2.5/forecast?lat={}&lon={}&units=metric&lang={}&appid={}'
LANG = 'ru'


def get_location(city: str) -> tuple:
    url_city = URL_CITY.format(city, OPEN_WEATHER_API_KEY)
    try:
        r = requests.get(url_city)
        data = r.json()
        return data[0]['lat'], data[0]['lon']
    except Exception as e:
        print(e)
        print('Ошибка получения координат')


def dt_convert(ts: int) -> str:
    _format = '%Y-%m-%d %H:%M:%S'
    return datetime.datetime.fromtimestamp(ts).isoformat()


def weather(lat: float, lon: float) -> dict:
    url = URL.format(lat, lon, LANG, OPEN_WEATHER_API_KEY)
    try:
        response = requests.get(url).json()
        length_day = response['city']['sunset'] - response['city']['sunrise']
        data = {
            'first_timestamp': dt_convert(response['list'][0]['dt']),
            'city': response['city']['name'],
            'timezone': response['city']['timezone'],
            'length_day': length_day // 3600,
            'weather': response['list'][0]['weather'][0]['description'].capitalize(),
            'temp': response['list'][0]['main']['temp'],
            'pressure': response['list'][0]['main']['pressure'],
            'humidity': response['list'][0]['main']['humidity'],
        }
        pprint(data)
        return data

    except Exception as e:
        print(e)
        print('Ошибка получения погоды')


def get_weather(text: str) -> str:
    city = text.strip()
    lat, lon = get_location(city)
    weather(lat, lon)
    answer = ''
    return answer


if __name__ == '__main__':
    get_weather('Moscow')
