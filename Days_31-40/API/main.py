import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")

print(f"Response text -> {response.text}")
print(f"Response status code {response.status_code}")
print(f"ISS position {response.json()['iss_position']}")
print(f"ISS position longitude {response.json()['iss_position']['longitude']}")