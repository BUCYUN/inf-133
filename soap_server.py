from http.server import HTTPServer
from pysimplesoap.server import SoapDispatcher, SOAPHandler

def saludar(nombre):
 return "Hola, {}! " .format(nombre)

dispatcher = SoapDispatcher{
 "ejemplo-soap-server",
 location="http://localhost:8000/",
 action="http://localhost:8000/",
}