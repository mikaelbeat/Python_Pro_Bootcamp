
data = {
    "Bug1": "Error in opening page.",
    "Bug2": "Error while saving.",
    "Bug3": "Error when logging out."
    }

print(data["Bug1"])

data["Bug3"] = "Error in memory usage."

print(data)

for key in data:
    print(f"{key} -> {data[key]}")
    
print("\n****************************\n")

travel_log = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    }
]
