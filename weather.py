import requests
from pprint import pprint
from config import X_GISMETEO_TOKEN

URL = 'https://api.gismeteo.net/v2/weather/current/4368/'


def get_weather(city):
    headers = {
        'X-Gismeteo-Token': '56b30cb255.3443075'
    }
    session = requests.Session()
    session.headers.update(headers)
    try:
        r = session.get(URL)
        print(session.headers)
        print(r.headers)
        data = r.json()
        pprint(data)
    except Exception as e:
        print(e)
        print('Ошибка')


def main():
    city = 'Moscow'
    get_weather(city)


if __name__ == '__main__':
    main()
