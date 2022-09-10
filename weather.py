import requests
import json

API_KEY = 'api-key' # api key from openweathermap.org site
CITY_NAME = 'city-name' # target city name

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

# get city location
location = get_city() # return tuple

# get weather wiht city lat and lon data
weather = get_weather(location[0], location[1]) # return dic

# simple show data
print(weather['main']['temp'])