import requests

url = "http://localhost:8000/"

ruta_get = url + "lista_estudiantes"
get_response = requests.request(method="GET", url=ruta_get)
print(get_response.text)

ruta_post = url + "agrega_estudiante"

nuevo_estudiante = {
    "nombre": "Juanito","apellido": "Perez","carrera": "Ingenieria Agronomica"
}

post_response = requests.request(method="POST", 
                                    url=ruta_post, 
                                    json=nuevo_estudiante)




print(post_response.text)