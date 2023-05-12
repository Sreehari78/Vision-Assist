import json
from urllib.request import urlopen
import debian
from requests import request


LOCATION_URL = 'http://ipinfo.io/json'
WEATHER_URL = 'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}'
WEATHER_API = '32c16013b8f339f44489182bf00baeb1'


class weatherLocation:
    def __init__(self,flag1,flag2):
        self.flag1 = flag1
        self.flag2 = flag2

    def loc_weather(self):
        if self.flag1:
            response = urlopen(LOCATION_URL)
            data = json.load(response)
            location = data['loc'].split(',')
            latitude = location[0]
            longitude = location[1]
            city = data['city']

            if self.flag2:
                WEATHER_URL.replace('{lat}', latitude)
                WEATHER_URL.replace('{lon}', longitude)
                WEATHER_URL.replace('{API key}', WEATHER_API)
                res = request.get(WEATHER_URL)
                condition = res['weather'][0]['main']
                description = res['weather'][0]['description']
            
            if self.flag1 == True and self.flag2 == True:
                return condition, description
            else:
                return city