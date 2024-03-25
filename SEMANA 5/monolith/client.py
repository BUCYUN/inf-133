import requests
url = "http://localhost:8000"

response = requests.get(f"{url}/posts")

print(response.text)

nuevo_post = {
    3: {
        "title":"Mxperiencia como dev",
        "content" : "En Progreso"
    }
}
response = requests.post(f"{url}/posts/3", json=nuevo_post)
print(response.text)