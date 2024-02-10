import requests
from datetime import datetime
pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = "mikazaki"
TOKEN = ""

user_parameter = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_parameter)
#
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_parameter = {
    "id": "graph1",
    "name": "Habit Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}


today = datetime.now()
print(today.strftime("%Y%m%d"))

headers = {
    "X-USER-TOKEN": TOKEN
}
# response = requests.post(url=graph_endpoint, json=graph_parameter, headers=headers)

data_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1"

data_parameter = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "15"
}

# response = requests.post(url=data_endpoint, json=data_parameter, headers=headers)

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/{today.strftime('%Y%m%d')}"

update_parameter = {
    "quantity": "16"
}
# response = requests.put(url=update_endpoint, json=update_parameter, headers=headers)


delete_endpoint= f"{pixela_endpoint}/{USERNAME}/graphs/graph1/{today.strftime('%Y%m%d')}"

response = requests.delete(url=delete_endpoint, headers=headers)
