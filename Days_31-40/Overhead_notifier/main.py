
import requests
from datetime import datetime

MY_LAT = 60
MY_LONG = 25
MARGIN_OF_ERROR = 5

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

def check_location_and_time():
    iss_response = requests.get("http://api.open-notify.org/iss-now.json")
    iss_response.raise_for_status()
    data = iss_response.json()
    latitude = float(data["iss_position"]["latitude"])
    longitude = float(data["iss_position"]["longitude"])
    
    # latitude = MY_LAT
    # longitude = MY_LONG
    
    if round(latitude) <= 55 or round(latitude) >= 65 | round(longitude) <= 20 or round(longitude) >= 30:
        print("ISS is too far away.")
    else:
        time_response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
        time_response.raise_for_status()
        data = time_response.json()

        sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
        sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
        
        time_now = datetime.now()
        
        if int(sunrise) < int(time_now.hour) and int(sunset) > int(time_now.hour):
            print("It's too light to see ISS.")
        else:
            print("Look to the sky, ISS should be visible!")



check_location_and_time()