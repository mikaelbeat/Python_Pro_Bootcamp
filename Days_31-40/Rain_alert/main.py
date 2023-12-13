
import requests
import os


BASEURL = "http://api.openweathermap.org/data/2.5/forecast"
API_KEY = os.environ.get("AUTH_TOKEN")
LATITUDE = 60.169857
LONGITUDE = 24.938379


parameters = {
    "lat": LATITUDE,
    "lon": LONGITUDE,
    "cnt": 4,
    "appid": API_KEY
}


response = requests.get(BASEURL, params=parameters)
response.raise_for_status()
data = response.json()


#print(data["list"][0]["weather"][0]["id"])

will_rain = False
for weather in data["list"]:
    weather_condition = (weather["weather"][0]["id"])
    if int(weather_condition) < 700:
        will_rain = True
if will_rain:
    print("Bring umbrella!")