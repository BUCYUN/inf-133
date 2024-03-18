import requests

url = "http://localhost:8000/delivery"

headers = {"Content-Type": "application/json"}

vehicle_type = "drone"
data = {"vehicle_type": vehicle_type}

response = requests.post(url, json=data, headers=headers)

if response.status_code == 200:
    print(response.text)
else:
    print("Error scheduling delivery:", response.text)
    