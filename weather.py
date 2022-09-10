import requests
import json

API_KEY = '519ab2b1a1cc790599a1052ba62c74e4'
CITY_NAME = 'zanjan'

def get_city():
    response = requests.get(f'http://api.openweathermap.org/geo/1.0/direct', params={
        'q' : CITY_NAME,
        'appid' : API_KEY,
    })

    data = json.loads(response.content)

    return data[0]['lat'], data[0]['lon']

def get_weather(lat, lon):
    response = requests.get(f'https://api.openweathermap.org/data/2.5/weather', params={
        'lat' : lat,
        'lon' : lon,
        'appid' : API_KEY,
        'units' : 'metric',
    })

    data = json.loads(response.content)

    return data

location = get_city()
weather = get_weather(location[0], location[1])

print(weather['main']['temp'])