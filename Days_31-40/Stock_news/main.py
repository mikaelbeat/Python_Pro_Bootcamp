import requests
import os
import json
from datetime import date, timedelta

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_API_KEY = os.environ.get("STOCK_API_KEY")

NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")

API_KEY = ""
# STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").


stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
}

today = date.today()
yesterday = today - timedelta(days= 1)
day_before_yesterday = today - timedelta(days= 4)



# TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
response = requests.get(STOCK_ENDPOINT, params=stock_parameters)
response.raise_for_status()
data = response.json()

yesterday_closing_prise = data["Time Series (Daily)"][str(yesterday)]["4. close"]
print(yesterday_closing_prise)

#TODO 2. - Get the day before yesterday's closing stock price
day_before_yesterday_closing_prise = data["Time Series (Daily)"][str(day_before_yesterday)]["4. close"]
print(day_before_yesterday_closing_prise)


#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
closing_price_difference = float(yesterday_closing_prise) - float(day_before_yesterday_closing_prise)
positive_difference = abs(closing_price_difference)
print(positive_difference)

#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
percentage_difference = int(((float(day_before_yesterday_closing_prise) - float(yesterday_closing_prise)) * 100) / float(yesterday_closing_prise))
print(percentage_difference)

#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
news_parameters = {
    "q": COMPANY_NAME,
    "apikey": NEWS_API_KEY
}

if percentage_difference > 5:
    response = requests.get(NEWS_ENDPOINT, params=news_parameters)
    response.raise_for_status()
    data = response.json()

    print(f"\nGetting related news on {COMPANY_NAME}.")
    for entry in range(3):
        print(data["articles"][entry]["title"])