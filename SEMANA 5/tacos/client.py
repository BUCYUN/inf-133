import requests

url = "http://localhost:8000/tacos"
headers = {'Content-type': 'application/json'}

response = requests.get(url)
print(response.json())

# POST /tacos 
mi_taco = {
    "base": "Tortilla",
    "guiso": "Res",
    "toppings": ["Jamon", "Pulpa"],
    "salsa" : "Chile"
}
response = requests.post(url, json=mi_taco, headers=headers)
print(response.json())

response = requests.get(url)
print(response.json())

# PUT /tacos/1
edit_taco = {
    "base": "Tortilla",
    "guiso": "Cerdo",
    "toppings": ["Jamon", "Molida"],
    "salsa" : "tomate"
}
response = requests.put(url+"/1", json=edit_taco, headers=headers)
print(response.json())

response = requests.get(url)
print(response.json())

# DELETE /tacos/1
response = requests.delete(url + "/1")
print(response.json())

response = requests.get(url)
print(response.json())