import requests
from datetime import datetime
import time
import smtplib

MY_EMAIL = "davidbengtsson321@gmail.com"
PASSWORD = ""

# Eslöv lat/lon
MY_LAT = 55.839260 # Your latitude
MY_LONG = 13.303820 # Your longitude



def iss_station_overhead():

    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    print(iss_latitude, iss_longitude)

    if MY_LAT > iss_latitude +5 or MY_LAT < iss_latitude -5:
        if MY_LONG > iss_longitude +5 or MY_LONG < iss_longitude -5:
            print("False")
            return False
    print("True")
    return True



#Your position is within +5 or -5 degrees of the ISS position.

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])



    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

while True:
    time.sleep(60)
    if iss_station_overhead() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(MY_EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject: Look up\n\nThe ISS is above you in the sky."
        )
