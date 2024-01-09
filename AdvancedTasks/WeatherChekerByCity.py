import os
import requests
def weatherCheker(city):
    api_key = os.environ.get('API_KEY')
    base_url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    response = requests.get(base_url)
    data = response.json()
    if response.status_code == 200:
        print(f'Weather in {city} : {data["weather"][0]["description"]} (temp is {data["main"]["temp"]})')
    else:
        print(f'Failed to fetch weather inforamtion. {response}')

city = 'Warsaw'
weatherCheker(city)