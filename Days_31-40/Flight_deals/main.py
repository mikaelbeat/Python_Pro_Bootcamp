import data_manager
import flight_data
import flight_search
import notification_manager

import requests
import os
from datetime import datetime
from pprint import pprint


KIWI_API_KEY = os.environ.get("KIWI_API_KEY")
KIWI_ENDPOINT = "https://api.tequila.kiwi.com/locations/query"

SHEETY_ENDPOINT = "https://api.sheety.co/6dcd4d27c2bd18b70b19ec268c6d28b0/flightDeals/prices"

date = datetime.now()
TODAY = date.strftime("%d.%m.%Y")
TIME = date.strftime("%H:%M")

kiwi_headers = {
    "apikey": KIWI_API_KEY
}


sheety_response = requests.get(url=SHEETY_ENDPOINT)
sheety_result = sheety_response.json()
citien_list_size = len(sheety_result["prices"])




for entry in range(citien_list_size):
    sheety_id = sheety_result["prices"][entry]["id"]
    city = sheety_result["prices"][entry]["city"]
    iataCode = sheety_result["prices"][entry]["iata"]
    
    if iataCode == "":
        kiwi_request = {
            "term" : city,
            "location_types": "city"
        }

        kiwi_response = requests.get(url=KIWI_ENDPOINT, headers=kiwi_headers, params=kiwi_request)
        kiwi_result = kiwi_response.json()
        city_iata_code = kiwi_result["locations"][0]["code"]
                
        new_data = {
                "price": {
                    "iata": city_iata_code
                }
            }
        
        response = requests.put(url=f"{SHEETY_ENDPOINT}/{sheety_id}", json=new_data)
    else:
        pass