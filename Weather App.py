# Weather App
# Given a city name or zip code, returns the weather for that area

import requests
import re

# Access Weather API
api_key = 'Replace with your API key from api.openweathermap.org'

# URLs: Get weather by city name or zip code
name = 'https://api.openweathermap.org/data/2.5/weather?q=replace&appid=api_key&units=imperial'
zip = 'https://api.openweathermap.org/data/2.5/weather?zip=replace&appid=api_key&units=imperial'
# add &units=imperial for imperial

# User Input
location = input('City Name or Zip Code? ').replace(' ', '+')

# Checks if input is a name or zip code
if re.match('\d',location):
    url = zip
else:      
    url = name

url = url.replace('replace', location).replace('api_key', api_key)

response = requests.get(url).json() # returns json file from weather API

weather_info = response
city_name = weather_info['name']
feel_like = weather_info['main']['feels_like']
high = weather_info['main']['temp_max']
low = weather_info['main']['temp_min']
desc = weather_info['weather'][0]['description']

print(f'The weather in {city_name} feels like {feel_like}°F with a low of {low}°F, high of {high}°F with {desc}')