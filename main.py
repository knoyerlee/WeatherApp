# Use an API to get weather data and display it in a GUI format 
# TODO Display weather data in a meaninful way look at other apps and what they use

from weatherfunctions import Temperature as t
import requests
import json
import os

token = (os.getenv('WEATHERTOKEN'))

# Temps are retrieved in kelvin will need to convert to F and C (now have class to do this with labels)
while (True):
    # Request some city input from the user
    city_name = input('Please enter the city you are located in: ')
    api_url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name.title()}&appid={token}"
    
    # Stores the response from the api in a variable
    api_response = requests.get(api_url)
    
    # tatkes the stored response and converts it into json text format
    weather_content = json.loads(api_response.text)

    try:
        temperature = weather_content['main']['temp']
        feels_like = weather_content['main']['feels_like']
        temp_low = weather_content['main']['temp_min']
        temp_high = weather_content['main']['temp_max']
        humidity = weather_content['main']['humidity']
        if (humidity):
            break
    except:
        print('invalid city')

print(temperature)