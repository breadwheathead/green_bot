import json
import datetime
import requests
from pprint import pprint
from config import OPEN_WEATHER_API_KEY

URL_CITY = 'http://api.openweathermap.org/geo/1.0/direct?q={}&&appid={}'
URL = 'http://api.openweathermap.org/data/2.5/forecast?lat={}&lon={}&units=metric&lang={}&appid={}'
LANG = 'ru'

WEATHER_EMOJI = {
    'Clear': 'Ясно \U00002600',
    'Clouds': 'Облачно \U00002601',
    'Rain': 'Дождь \U00002614',
    'Drizzle': 'Дождь \U00002614',
    'Thunderstorm': 'Гроза \U000026A1',
    'Snow': 'Снег \U0001F328',
    'Mist': 'Туман \U0001F32B'
}


def get_weather(text):
    city = text.strip()
    lat, lon = get_location(city)
    weather = get_weather_param(lat, lon)
    return weather


def get_location(city: str) -> tuple:
    url_city = URL_CITY.format(city, OPEN_WEATHER_API_KEY)
    try:
        r = requests.get(url_city)
        data = r.json()
        # with open('weather_1.json', 'w', encoding='utf-8') as f:
        #     json.dump(data, f)
        lat = data[0]['lat']
        lon = data[0]['lon']
        return lat, lon
    except Exception as e:
        print(e.args)
        print('Ошибка получения координат')


def get_weather_param(lat: float, lon: float) -> str:
    url = URL.format(lat, lon, LANG, OPEN_WEATHER_API_KEY)
    try:
        response = requests.get(url).json()
        # length_day = response['city']['sunset'] - response['city']['sunrise']

        # 'first_timestamp': dt_convert(response['list'][0]['dt'])
        city = response['city']['name']
        # 'timezone': response['city']['timezone']
        # 'length_day': length_day // 3600,
        temp = response['list'][0]['main']['temp']
        pressure = response['list'][0]['main']['pressure']
        humidity = response['list'][0]['main']['humidity']
        weather_main = response['list'][0]['weather'][0]['main']
        if weather_main in WEATHER_EMOJI:
            wd = WEATHER_EMOJI[weather_main]
        else:
            wd = 'Это мужицкий дождь \U0001F4AA ! Аллилуйя! 🙌'

        answer = f'Погода в городе {city}\n' \
                 f'{wd}\n' \
                 f'Температура: {temp} °C\n' \
                 f'Давление: {pressure} мм рт. ст.\n' \
                 f'Влажность: {humidity} %\n'

        return answer

    except Exception as e:
        print(e)
        print('Ошибка получения погоды')


def dt_convert(ts: int) -> str:
    _format = '%Y-%m-%d %H:%M:%S'
    return datetime.datetime.fromtimestamp(ts).isoformat()


if __name__ == '__main__':
    print(get_weather('Moscow'))
