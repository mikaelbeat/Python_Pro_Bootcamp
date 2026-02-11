
import pandas
import csv


# Read the CSV file and extract the temperatures
with open('weather_data.csv', 'r') as file:
    reader = csv.reader(file)
    temperatures = [int(data[1]) for data in reader if data[1].isdigit()]
    print(temperatures)
     
print("\n*********************************************\n")

# Using pandas to read the CSV file and extract the temperatures
data = pandas.read_csv('weather_data.csv')
print(data['temp'])

print(data['temp'].mean())
print(data['temp'].max())

print("\n*********************************************\n")

# Get data in columns
print(data[data.day == "Monday"])
print("\n")
print(data[data.temp == data.temp.max()])

print("\n*********************************************\n")

# Get data in rows
monday = data[data.day == "Monday"]
print(monday.condition)

print("\n*********************************************\n")

# Create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
data.to_csv('new_data.csv')
print(data)