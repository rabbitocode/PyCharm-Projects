import os
import requests
from datetime import *

date_now = date.today()
now = datetime.now()

date = date_now.strftime("%Y/%m/%d")
current_time = now.strftime("%H:%M:%S")

APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")
ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise/"
SHEETY_ENDPOINT = "https://api.sheety.co/83b361a4c33c1348929aa3efc41aea05/myWorkoutsPythonProject/workouts"
AUTH_TOKEN = os.environ.get("AUTH_TOKEN")


GENDER = "male"
WEIGHT_KG = "82"
HEIGHT_CM = "182"
AGE = "20"


exercise_text = "I ran for 6 hour"


params = {
    "query": exercise_text.title(),
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}


sheety_header = {
    "Authorization": "Bearer OJ3i2913KOSAKE-,dkasmdjub#IJjn31"
}


response = requests.post(url=ENDPOINT, json=params, headers=headers)
response.raise_for_status()
result = response.json()

print(result)
print(date)
print(current_time)


for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": date,
            "time": current_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(SHEETY_ENDPOINT, json=sheet_inputs, headers=sheety_header)
    sheet_response.raise_for_status()

    print(sheet_response.text)






