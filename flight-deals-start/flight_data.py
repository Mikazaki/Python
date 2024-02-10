from pprint import pprint
import requests
class FlightData:
    def __init__(self):
        self.sheet_endpoint = "https://api.sheety.co/be46e938eb670a78f145b860c2d448a5/flightDeals/prices"
        headers = {
            "Authorization": "Bearer ffgbfdbcvbgt5rt5646ert4"
        }
        self.response = requests.get(url= self.sheet_endpoint, headers=headers)




