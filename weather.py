import requests
from pprint import pprint
from config import OPEN_WEATHER_API_KEY

URL_CITY = 'http://api.openweathermap.org/geo/1.0/direct?q={}&&appid={}'
URL = 'http://api.openweathermap.org/data/2.5/forecast?lat={}&lon={}&appid={}'


def get_location(city: str) -> tuple:
    url_city = URL_CITY.format(city, OPEN_WEATHER_API_KEY)
    try:
        r = requests.get(url_city)
        data = r.json()
        return data[0]['lat'], data[0]['lon']
    except Exception as e:
        print(e)
        print('Ошибка получения координат')


def get_weather(lat, lon):
    url = URL.format(lat, lon, OPEN_WEATHER_API_KEY)
    try:
        r = requests.get(url)
        data = r.json()
        pprint(data)
    except Exception as e:
        print(e)
        print('Ошибка получения погоды')


def main():
    city = 'phuket'
    lat, lon = get_location(city)
    get_weather(lat, lon)


if __name__ == '__main__':
    main()
