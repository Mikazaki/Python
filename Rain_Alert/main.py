import requests
from twilio.rest import Client


api_key = ""
account_sid = ""
auth_token = ""

parameters = {
    "lat": ,
    "lon": ,
    "exclude": "current,minutely,daily",
    "appid": ""

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
