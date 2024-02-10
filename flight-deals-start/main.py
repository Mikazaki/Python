#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from pprint import pprint
from flight_data import FlightData
from flight_search import FlightSearch
import requests

data = FlightData()
iata = FlightSearch()

response = requests.put(url="https://api.sheety.co/be46e938eb670a78f145b860c2d448a5/flightDeals/prices/[Object ID]")
sheet_data = data.response.json()["prices"]

for code in sheet_data:
    codes = code["iataCode"]


pprint(sheet_data)