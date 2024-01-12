import data_manager
import flight_data
import flight_search
import notification_manager

import requests
import os
from datetime import datetime
from pprint import pprint


NUTRI_APP_ID = os.environ.get("NUTRI_APP_ID")
NUTRI_API_KEY = os.environ.get("NUTRI_API_KEY")
NUTRI_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

SHEETY_ENDPOINT = "https://api.sheety.co/6dcd4d27c2bd18b70b19ec268c6d28b0/flightDeals/prices"

date = datetime.now()
TODAY = date.strftime("%d.%m.%Y")
TIME = date.strftime("%H:%M")


response = requests.get(url=SHEETY_ENDPOINT)
result = response.json()
# pprint(result)

citien_list_size = len(result["prices"]) - 1
print(citien_list_size)

iataCode_body = {
    "iataCode": "TESTING"
}

for entry in range(citien_list_size):
    iataCode = result["prices"][entry]["iataCode"]
    if iataCode == "":
        print("Oli tyhjä")
        response = requests.put(url=SHEETY_ENDPOINT + [entry]["iataCode"], json=iataCode_body)
    else:
        print("Oli jotain")