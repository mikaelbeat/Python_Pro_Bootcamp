
import requests
from datetime import datetime

date = datetime.now()

TODAY = date.strftime("%Y%m%d")
USERNAME = "mikaelbeat"
TOKEN = "r230t9u234t932t02"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
add_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
update_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{TODAY}"


################ CREATE USER ##################

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)

################ CREATE GRAPH ##################

headers = {
    "X-USER-TOKEN": TOKEN
}

graph_config = {
    "id": GRAPH_ID,
    "name": "Coding",
    "unit": "Hour",
    "Type": "float",
    "color": "shibafu"
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)

################ CREATE PIXEL ##################

headers = {
    "X-USER-TOKEN": TOKEN
}

pixel_data = {
    "date": TODAY,
    "quantity": "2",
    "optionalData": '{"Lanquage": "Python"}'
}

# response = requests.post(url=add_pixel_endpoint, json=pixel_data, headers=headers)

################ UPDATE PIXEL ##################

headers = {
    "X-USER-TOKEN": TOKEN
}

update_pixel = {
    "quantity": "5"
}

# response = requests.put(url=update_pixel_endpoint, json=update_pixel, headers=headers)

################ DELETE PIXEL ##################

headers = {
    "X-USER-TOKEN": TOKEN
}

response = requests.delete(url=update_pixel_endpoint, headers=headers)