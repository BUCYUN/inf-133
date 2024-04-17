import requests

url = 'http://localhost:5000/'

response = requests.get(url)
print(response.text)

params = {'nombre': 'Brayan'}
response = requests.get(url+'saludar', params=params)
print (response.json())

params = {'num1':5, 'num2':3}
response = requests.get(url+'sumar', params=params)
print (response.json())

params = {'cadena' : 'reconocer'}
response = requests.get(url+'palindromo', params=params)
print (response.json())

params = {'cadena' : 'exepciones', 'vocal': 'e'}
response = requests.get(url+'contar', params=params)
print (response.json())

