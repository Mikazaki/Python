import requests
from datetime import datetime

APP_ID = "e2f844b7"
API_KEY = "36230fdd0a4676370f86d0ada2f3953d"
GENDER = "female"
WEIGHT_KG = 64
HEIGHT_CM = 175
AGE = 18

now = datetime.now()
today = now.strftime("%Y/%m/%d")
time = now.strftime("%H:%M:%S")

exercise_text = input("What exercise(s) did you do: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}


exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_parameter = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

sheety_endpoint = "https://api.sheety.co/be46e938eb670a78f145b860c2d448a5/workoutTracking/workouts"

response = requests.post(url=exercise_endpoint, json=exercise_parameter, headers=headers)
result = response.json()

for excercises in result["exercises"]:
    data_inputs = {
        "workout": {
            "date": today,
            "time": time,
            "exercise": excercises["name"].title(),
            "duration": excercises["duration_min"],
            "calories": excercises["nf_calories"]
        }
    }

    bearer_headers = {
        "Authorization": "Bearer stert3495u9r0euirdjhgi34ht98hdf"
    }
    sheets = requests.post(url=sheety_endpoint, json=data_inputs, headers=bearer_headers)
    print(sheets.text)
