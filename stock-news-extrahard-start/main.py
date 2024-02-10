import requests
from datetime import datetime, timedelta
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "tesla"

API_KEY = "981U5T8FBAGN3KFW"

API_KEY_NEWS = "f963eeeea6d44b6a90f073a813fcd477"

account_sid = "ACa20a3c9d2510e8075068c3737f19dce2"
auth_token = "6619cf5705678c8e472d2bbcaa7ba0b4"
client = Client(account_sid, auth_token)

parameter = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "outputsize": "full",
    "apikey": API_KEY
}

today = datetime.now().date()

yesterday = today - timedelta(days=1)

day_before_yesterday = today - timedelta(days=2)

parameter_news = {
    "q": COMPANY_NAME,
    "from": yesterday,
    "sortBy": "popularity",
    "apiKey": API_KEY_NEWS
}

response = requests.get(url='https://www.alphavantage.co/query?', params=parameter)
response.raise_for_status()

news = requests.get(url="https://newsapi.org/v2/everything", params=parameter_news)
data = response.json()
articles = news.json()

article_list = articles["articles"][:3]

headline = ""
description = ""

yesterday_close = float(data["Time Series (Daily)"][str(yesterday)]["4. close"])
day_before_yesterday_close = float(data["Time Series (Daily)"][str(day_before_yesterday)]["4. close"])

increase = ((yesterday_close - day_before_yesterday_close) / day_before_yesterday_close) * 100

if increase >= 5 or increase <= -5:
    for article in article_list:
        headline = article["title"]
        description = article["description"]

        if increase >= 5:
            message = client.messages.create(
                body=f"{STOCK}: 🔺{round(increase, 2)}%\nHeadline: {headline}\nBrief: {description}\n",
                from_='+12057917118',
                to='+13439966636'
            )
            print(message.status)

        else:
            message = client.messages.create(
                body=f"{STOCK}: 🔻{abs(round(increase, 2))}%\nHeadline: {headline}\nBrief: {description}\n",
                from_='+12057917118',
                to='+13439966636'
            )
            print(message.status)
