#Global Weather Program
import datetime
import requests

API_KEY = "9534b6a5e499fba2db4c719caf823fd3"


BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"


def convert_temp(kelvin): 

    celsius = kelvin - 273.15

    fahrenheit = (celsius * (9/5)) + 32

    return celsius, fahrenheit
 

def get_weather_info(city):
    
    URL = BASE_URL + "appid=" + API_KEY + "&q=" + city
    response = requests.get(URL).json()

    temp_kelvin = response['main']['temp']

    temp_celsius, temp_fahrenheit = convert_temp(temp_kelvin)

    humidity = response['main']['humidity']

    wind_speed = response['wind']['speed']

    feels_like_c, feels_like_f = map(int, convert_temp(response['main']['feels_like']))

    info = "\nWeather information for {}".format(city)
    print(info.title())
    print("Temperature: {:0.01f}°C".format(temp_celsius) + ", {:0.01f}°F".format(temp_fahrenheit))
    print("Humidity: {}%".format(humidity))
    print("Wind Speed: {}m/s".format(wind_speed))
    print("Feels Like: {:0.01f}°C".format(feels_like_c) + ", {:0.01f}°F".format(feels_like_f))
    print("\n\n")


run = True
while run:

    city = input("Enter a city to get its weather data or X to exit: ")

    if city.upper() == "X":
        run = False

        
    get_weather_info(city)

    
