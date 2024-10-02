import requests
from datetime import datetime

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
#
#
# data = response.json()["iss_position"]
#
#
# longitude = response.json()["iss_position"]["longitude"]
# latitude = response.json()["iss_position"]["latitude"]
#
# iss_position = (longitude,latitude)
#
# print(iss_position)

MY_LATITUDE = 55.839260
MY_LONGITUDE = 13.303820



parameters = {
    "lat": MY_LATITUDE,
    "lng": MY_LONGITUDE,
    "formatted": 0,
}



response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()

data = response.json()

sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]



print(sunrise)
print(sunset)

time_now = datetime.now()

print(time_now.hour)
