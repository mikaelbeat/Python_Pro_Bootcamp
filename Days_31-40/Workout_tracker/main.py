
import requests
import os
from datetime import datetime


NUTRI_APP_ID = os.environ.get("NUTRI_APP_ID")
NUTRI_API_KEY = os.environ.get("NUTRI_API_KEY")
NUTRI_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

SHEETY_ENDPOINT = "https://api.sheety.co/6dcd4d27c2bd18b70b19ec268c6d28b0/myWorkouts/workout"
SHEETY_BEARER = os.environ.get("SHEETY_BEARER")


date = datetime.now()
TODAY = date.strftime("%d.%m.%Y")
TIME = date.strftime("%H:%M")


headers = {
    "x-app-id": NUTRI_APP_ID,
    "x-app-key": NUTRI_API_KEY
}


request = {
    "query": "swim for 2 hour",
    "gender": "Male",
    "weight_kg": 81,
    "height_cm": 182,
    "age": 41
}

response = requests.post(url=NUTRI_ENDPOINT, json=request, headers=headers)
result = response.json()
calories = result["exercises"][0]["nf_calories"]
exercise = result["exercises"][0]["name"]
duration = result["exercises"][0]["duration_min"]


headers = {
    "Authorization": f"Bearer {SHEETY_BEARER}"
}

request = {
    "workout": {
        "date": TODAY,
        "time": TIME,
        "exercise": exercise,
        "duration": duration,
        "calories": calories
    }
}

response = requests.post(url=SHEETY_ENDPOINT, json=request, headers=headers)
result = response.json()