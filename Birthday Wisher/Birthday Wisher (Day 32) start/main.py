import smtplib
import datetime as dt
import random
import pandas











now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()

if year == 2020:
    print("Wear a face mask")




data_of_birth = dt.datetime(year=2003, month=10, day=17)



if day_of_week == 0:

    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)

    my_email = "davidbengtsson321@gmail.com"
    password = ""

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="rabbitoman123@gmail.com",
            msg=f"Subject:Motivational Quote\n\n{quote}"
        )