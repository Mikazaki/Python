import requests
from twilio.rest import Client


api_key = "7ea363a0f1ea35e3bc7c13ed2cb58874"
account_sid = "ACa20a3c9d2510e8075068c3737f19dce2"
auth_token = "6619cf5705678c8e472d2bbcaa7ba0b4"

parameters = {
    "lat": 67.4082508,
    "lon": -68.47072222222222,
    "exclude": "current,minutely,daily",
    "appid": "7ea363a0f1ea35e3bc7c13ed2cb58874"

}


response = requests.get(url="https://api.openweathermap.org/data/2.8/onecall", params=parameters)
response.raise_for_status()

data = response.json()
twelve_hour = data["hourly"][:12]

will_rain = False
for hours in twelve_hour:
    id = twelve_hour[0]["weather"][0]["id"]
    if id <= 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It is going to rain. Remember to bring an ☂️",
        from_='+12057917118',
        to='+13439966636'
    )
    print(message.status)