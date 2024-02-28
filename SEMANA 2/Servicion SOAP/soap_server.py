from http.server import HTTPServer
from pysimplesoap.server import SoapDispatcher,SOAPHandler

def saludar (nombre):
    return "¡Hola, {}!".format(nombre)

def SumaDosNumeros(x, y):
    res = x + y
    return 'la suma de {} y {} es: {}'.format(x,y,res)
    
def CadenaPalindromo(cadena):
    inicio = 0
    fin = len(cadena) - 1
    while inicio < fin:
        if cadena[inicio] != cadena[fin]:
            return False
        inicio += 1
        fin -= 1
    return True

dispatcher=SoapDispatcher(
    "Ejemplo-Soap-Server",
    location = "http://localhost:8000/", 
    action = "http://localhost:8000/", 
    namespace = "http://localhost:8000/", 
    trace = True, 
    ns=True
    )

dispatcher.register_function(
    "Saludar", 
    saludar, 
    returns={"saludo":str}, 
    args={"nombre":str}
    )

dispatcher.register_function(
    "SumaDosNumeros", 
    SumaDosNumeros, 
    returns={"resultado": str}, 
    args={"x":int, "y":int},
    )

dispatcher.register_function(
    "CadenaPalindromo", 
    CadenaPalindromo, 
    returns={"resultado": bool}, 
    args={"cadena":str},
    )

server = HTTPServer(("0.0.0.0",8000),SOAPHandler)

server.dispatcher=dispatcher

print("Servidor SOAP Iniciando en http://localhost:8000/")

server.serve_forever()