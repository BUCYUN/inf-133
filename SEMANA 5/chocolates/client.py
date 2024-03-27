import requests
import json

url = "http://localhost:8000/deliveries"
headers = {"Content-Type": "application/json"}

# POST /deliveries
new_chocolate_data = {
    "tipo": "tableta",
    "peso": "80 g",
    "sabor": "vainilla"
}
response = requests.post(url=url, json=new_chocolate_data, headers=headers)
print(response.json())

new_chocolate_data = {
    "tipo": "bombon",
    "peso": "180 g",
    "sabor": "fresa",
    "relleno": "choclate"
}
response = requests.post(url=url, json=new_chocolate_data, headers=headers)
print(response.json())


# GET /deliveries
response = requests.get(url=url)
print(response.json())

