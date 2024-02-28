from zeep import Client

client=Client("http://localhost:8000/")

#no se puede ejecutar los 3 al mismo tiempo

#result=client.service.Saludar(nombre="Brayan")
result=client.service.SumaDosNumeros(x = 5, y = 12)
#result=client.service.CadenaPalindromo(cadena = "somos")

print(result)