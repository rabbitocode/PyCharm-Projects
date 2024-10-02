import requests
import smtplib
from datetime import datetime, date, timedelta

today = date.today()
yesterday = today - timedelta(days=1)
two_days_ago = today - timedelta(days=2)

week = yesterday - timedelta(days=7)
to_date = yesterday

MY_EMAIL = "davidbengtsson321@gmail.com"
PASSWORD = "fdhveyrdpsqzghif"

NEWS_API = "e8a04019f74c4280b5b3cb064b77f311"
STOCK_API = "Ncaedkta_HS17kgHsz4hc3D2rvUDqWhq"

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla"

def SendEmail(recepient, subject, message):
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, PASSWORD)
        email_message = f"Subject: {subject}\n\n{message}"
        connection.sendmail(MY_EMAIL, recepient, email_message.encode('utf-8'))

parameters = {
    "adjusted": "true",
    "sort": "desc",
    "apiKey": STOCK_API,
}

STOCK_ENDPOINT = f"https://api.polygon.io/v2/aggs/ticker/{STOCK_NAME}/range/1/day/{week}/{to_date}"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

response = requests.get(STOCK_ENDPOINT, params=parameters)
response.raise_for_status()
data = response.json()

close_list = [x["c"] for x in data["results"]]

a = close_list[0] * 0.05
b = close_list[1] - close_list[0]

print(a)
print(b)

yesterday_close = data["results"][0]["c"]
two_days_ago_close = data["results"][1]["c"]

print(data)
print(f"Yesterday close was: {yesterday_close}")
print(f"Two Days ago close was : {two_days_ago_close}")

difference = yesterday_close - two_days_ago_close
up_down = "🔺" if difference > 0 else "🔻"

diff_percent = round((difference / two_days_ago_close) * 100, 2)

print(f"Difference: {difference}")
print(f"Diff Percent: {diff_percent}%")

if abs(diff_percent) > 1:
    print(f"Fetching news for {COMPANY_NAME}...")
    news_parameters = {
        "apiKey": NEWS_API,
        "qInTitle": COMPANY_NAME,
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_parameters)
    news_response.raise_for_status()
    articles = news_response.json()["articles"]

    three_articles = articles[:3]

    formatted_articles = [f"Headline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]

    for article in formatted_articles:
        SendEmail("rabb", f"{STOCK_NAME}: {up_down}{diff_percent}%", article)
else:
    print("Percentage change is not greater than 1%")