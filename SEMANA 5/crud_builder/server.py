from http.server import BaseHTTPRequestHandler, HTTPServer
import json

# Base de datos simulada de tacos
tacos = {}


# Producto: taco
class taco:
    def __init__(self):
        self.tamaño = None
        self.masa = None
        self.toppings = []

    def __str__(self):
        return f"Tamaño: {self.tamaño}, Masa: {self.masa}, Toppings: {', '.join(self.toppings)}"


# Builder: Constructor de tacos
class tacoBuilder:
    def __init__(self):
        self.taco = taco()

    def set_tamaño(self, tamaño):
        self.taco.tamaño = tamaño

    def set_masa(self, masa):
        self.taco.masa = masa

    def add_topping(self, topping):
        self.taco.toppings.append(topping)

    def get_taco(self):
        return self.taco


# Director: Pizzería
class Pizzeria:
    def __init__(self, builder):
        self.builder = builder

    def create_taco(self, tamaño, masa, toppings):
        self.builder.set_tamaño(tamaño)
        self.builder.set_masa(masa)
        for topping in toppings:
            self.builder.add_topping(topping)
        return self.builder.get_taco()


# Aplicando el principio de responsabilidad única (S de SOLID)
class tacoService:
    def __init__(self):
        self.builder = tacoBuilder()
        self.pizzeria = Pizzeria(self.builder)

    def create_taco(self, post_data):
        tamaño = post_data.get("tamaño", None)
        masa = post_data.get("masa", None)
        toppings = post_data.get("toppings", [])

        taco = self.pizzeria.create_taco(tamaño, masa, toppings)
        tacos[len(tacos) + 1] = taco
        
        return taco

    def read_tacos(self):
        return {index: taco.__dict__ for index, taco in tacos.items()}

    def update_taco(self, index, post_data):
        if index in tacos:
            taco = tacos[index]
            tamaño = post_data.get("tamaño", None)
            masa = post_data.get("masa", None)
            toppings = post_data.get("toppings", [])

            if tamaño:
                taco.tamaño = tamaño
            if masa:
                taco.masa = masa
            if toppings:
                taco.toppings = toppings

            return taco
        else:
            return None

    def delete_taco(self, index):
        if index in tacos:
            return tacos.pop(index)
        else:
            return None


class HTTPDataHandler:
    @staticmethod
    def handle_response(handler, status, data):
        handler.send_response(status)
        handler.send_header("Content-type", "application/json")
        handler.end_headers()
        handler.wfile.write(json.dumps(data).encode("utf-8"))

    @staticmethod
    def handle_reader(handler):
        content_length = int(handler.headers["Content-Length"])
        post_data = handler.rfile.read(content_length)
        return json.loads(post_data.decode("utf-8"))


# Manejador de solicitudes HTTP
class tacoHandler(BaseHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        self.controller = tacoService()
        super().__init__(*args, **kwargs)

    def do_POST(self):
        if self.path == "/tacos":
            data = HTTPDataHandler.handle_reader(self)
            response_data = self.controller.create_taco(data)
            HTTPDataHandler.handle_response(self, 200, response_data.__dict__)
        else:
            HTTPDataHandler.handle_response(self, 404, {"Error": "Ruta no existente"})

    def do_GET(self):
        if self.path == "/tacos":
            response_data = self.controller.read_tacos()
            HTTPDataHandler.handle_response(self, 200, response_data)
        else:
            HTTPDataHandler.handle_response(self, 404, {"Error": "Ruta no existente"})

    def do_PUT(self):
        if self.path.startswith("/tacos/"):
            index = int(self.path.split("/")[2])
            data = HTTPDataHandler.handle_reader(self)
            response_data = self.controller.update_taco(index, data)
            if response_data:
                HTTPDataHandler.handle_response(self, 200, response_data.__dict__)
            else:
                HTTPDataHandler.handle_response(
                    self, 404, {"Error": "Índice de taco no válido"}
                )
        else:
            HTTPDataHandler.handle_response(self, 404, {"Error": "Ruta no existente"})

    def do_DELETE(self):
        if self.path.startswith("/tacos/"):
            index = int(self.path.split("/")[2])
            deleted_taco = self.controller.delete_taco(index)
            if deleted_taco:
                HTTPDataHandler.handle_response(
                    self, 200, {"message": "taco eliminada correctamente"}
                )
            else:
                HTTPDataHandler.handle_response(
                    self, 404, {"Error": "Índice de taco no válido"}
                )
        else:
            HTTPDataHandler.handle_response(self, 404, {"Error": "Ruta no existente"})


def run(server_class=HTTPServer, handler_class=tacoHandler, port=8000):
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    print(f"Iniciando servidor HTTP en puerto {port}...")
    httpd.serve_forever()


if __name__ == "__main__":
    run()