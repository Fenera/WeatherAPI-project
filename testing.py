import datetime as dt
import requests

API_KEY = "9534b6a5e499fba2db4c719caf823fd3"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

city = "london"

def kelvin_to_celsius_farenheight(kelvin):
    celsius = kelvin - 273.15
    farenheight = celsius * (9/5) + 32

    return celsius, farenheight

URL = BASE_URL + "appid=" + API_KEY + "&q=" + city

response = requests.get(URL).json()

