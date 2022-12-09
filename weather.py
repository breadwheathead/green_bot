import json

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


def get_weather(lat: float, lon: float):
    url = URL.format(lat, lon, LANG, OPEN_WEATHER_API_KEY)
    try:
        response = requests.get(url).json()
        # with open('weather.json', 'w', encoding='utf-8') as f:
        #     json.dump(response, f, indent=2, ensure_ascii=False)

        data = {
            'city': response['city']['name'],
            'sunrise': response['city']['sunrise'],
            'sunset': response['city']['sunset'],
            'timezone': response['city']['timezone'],
            'first_timestamp': response['list'][0]['dt_txt'],
            'weather': response['list'][0]['weather'][0]['description'].capitalize(),
            'temp': response['list'][0]['main']['temp'],
            'humidity': response['list'][0]['main']['humidity'],
        }
        pprint(data)


    except Exception as e:
        print(e)
        print('Ошибка получения погоды')


def main():
    city = 'krasnoyarsk'
    lat, lon = get_location(city)
    get_weather(lat, lon)


if __name__ == '__main__':
    main()
