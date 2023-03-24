from dotenv import load_dotenv
import requests
import smtplib
import os

# This program sends news about tesla to an email when the stock price
# changes over 10% between two days.

# Password and api keys are stored in environment variables.
# Use your own email and app password/api keys if you want the code to work.
# You need separate ".env" file where you store your pass and api keys.

load_dotenv()

STOCK_API_KEY = os.environ.get("STOCK_API_KEY")
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")

MY_EMAIL = "jere.viitasalo@gmail.com"
PASSWORD = os.environ.get("PASSWORD")

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

stock_parameters = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
}
stock_data = requests.get(url=STOCK_ENDPOINT, params=stock_parameters)
stock_data.raise_for_status()
stock_data_json = stock_data.json()["Time Series (Daily)"]
stock_data_list = [value for (key,value) in stock_data_json.items()]

yesterday_data = stock_data_list[0]
day_before_yesterday_data = stock_data_list[1]

# Yesterday's closing stock price.
yesterday_closing_price = yesterday_data["4. close"]

# The day before yesterday's closing stock price
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]

# Price change between two days
price_change = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)

# Percentage difference in price between closing price yesterday and closing price the day before yesterday.
price_change_percent = round(price_change / float(day_before_yesterday_closing_price) * 100)

# If percentage is greater or less than 5 then get the first 3 news pieces for the COMPANY_NAME.
if price_change_percent > 0:
    price_emoji = "(UP)"
elif price_change_percent < 0:
    price_emoji = "(DOWN)"

if abs(price_change_percent) > 10:
    news_api_params = {
    "apiKey": NEWS_API_KEY,
    "q": COMPANY_NAME,
    "searchln": "title"
    }
    news_api_data = requests.get(NEWS_ENDPOINT, params=news_api_params)
    news_api_data.raise_for_status()
    articles = news_api_data.json()["articles"][:3]

# Creating a new list of the first 3 article's headline and description using list comprehension.
    formatted_articles = [f"Headline: {article['title']}.\nBrief: {article['description']}.\n" for article in articles]
    message = f"Subject: {STOCK_NAME} Price Change {price_emoji} {price_change_percent}%!\n\n"
    for article in formatted_articles:
        message += article

# Sending the news to email. 
    with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg=message.encode('utf-8'))