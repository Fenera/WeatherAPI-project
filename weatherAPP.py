import tkinter
import requests
import datetime



API_KEY = '9534b6a5e499fba2db4c719caf823fd3'

BASE_URL = 'http://api.openweathermap.org/data/2.5/weather?'


window = tkinter.Tk()
window.geometry('1280x720')
window.title('Weather Data')
window.config(bg='#9CC8D7')


def convert_temps(kelvin):

    celsius = int(kelvin - 273.15)
    fahrenheit = int(celsius * (9/5) + 32)

    return celsius, fahrenheit


def get_weather_data():

    temp_entry.delete(0, 'end')

    city = city_entry.get()

    URL = BASE_URL + 'appid=' + API_KEY + '&q=' + city
    
    response = requests.get(URL).json()

    temp_kelvin = response['main']['temp']

    temp_fahrenheit = (convert_temps(temp_kelvin))[1]

    temp_entry.insert(0, temp_fahrenheit)




#initialize all labels

city_label = tkinter.Label(window, text='City', bg='#9CC8D7')
city_entry = tkinter.Entry(window)

temp_f = tkinter.Label(window, text = 'Temp(F°)', bg='#9CC8D7')
temp_entry = tkinter.Entry(window)

enter_button = tkinter.Button(window, text='Search Data', command= get_weather_data)

#place labels on screen(grid, place, pack)

city_label.pack()
city_entry.pack()
temp_f.pack()
temp_entry.pack()
enter_button.pack()

















window.mainloop()





