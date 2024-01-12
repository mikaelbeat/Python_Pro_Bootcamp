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
citien_list_size = len(result["prices"]) - 1



for entry in range(citien_list_size):
    sheety_id = result["prices"][entry]["id"]
    city = result["prices"][entry]["city"]
    iataCode = result["prices"][entry]["code"]
    if iataCode == "":
        print("Oli tyhjä")
        new_data = {
                "price": {
                    "code": entry["code"]
                }
            }
        
        response = requests.put(url=f"{SHEETY_ENDPOINT}/{entry}", json=new_data)
    else:
        print("Oli jotain")
        
        
        
    #         response = requests.put(url=f"{SHEETY_ENDPOINT}/{sheety_id['id']}", json=new_data)
    # else:
    #     print("Oli jotain")