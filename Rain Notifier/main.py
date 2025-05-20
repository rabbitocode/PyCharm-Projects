import requests
import smtplib


MY_EMAIL = "davidbengtsson321@gmail.com"
PASSWORD = ""



# Inactive key
api_key = "a800293d2c9ac5a4fc24713fad372c1a"


ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"



# Eslöv lat/lon
MY_LAT = 55.839260 # Your latitude
MY_LONG = 13.303820 # Your longitude



# parameters = {
#     "key" : api_key,
#     "q": "Eslov",
#     "days": 1,
# }


parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
    "cnt": 4,
}


response = requests.get(ENDPOINT, params=parameters)
response.raise_for_status()
weather_data = response.json()









will_rain = False

for three_hours in weather_data["list"]:
    codes = three_hours["weather"][0]["id"]
    if codes <= 700:
        will_rain = True
if will_rain:
    print("Bring an Umbrella")
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(MY_EMAIL, PASSWORD)
    connection.sendmail(
        from_addr=MY_EMAIL,
        to_addrs="rabbit0060@gmail.com",
        msg="Rain\n\nIt will rain today bring an Umbrella"
    )

