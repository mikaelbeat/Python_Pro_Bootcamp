
import pandas

# Amount of squirrels by color using pandas method
data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
amount_by_color = data["Primary Fur Color"].value_counts()
print(amount_by_color)

# Amount of squirrels by color using dataframe
gray_squirrels = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels = len(data[data["Primary Fur Color"] == "Black"])

print("\n*********************************************\n")

# Create a new dataframe with the amount of squirrels by color
data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels, red_squirrels, black_squirrels]
}
df = pandas.DataFrame(data_dict)
print(df)

