from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "¡Hola, mundo!"

@app.route("/saludar", methods=["GET"])
def saludar():
    nombre = request.args.get("nombre")
    if not nombre:
        return (
            jsonify({"error": "Se requiere un nombre en los parámetros de la URL."}),
            400,
        )
    return jsonify({"mensaje": f"¡Hola, {nombre}!"})

@app.route("/sumar", methods=["GET"])
def sumar():
    num1 = request.args.get("num1")
    num2 = request.args.get("num2")
    if not num1:
        return jsonify({"error": "num1 no existe"})
    if not num2:
        return jsonify({"error": "num2 no existe"})
    res = int(num1)+int(num2)
    return jsonify({"resultado": res})

@app.route("/palindromo", methods=["GET"])
def palindromo():
    cadena = request.args.get("cadena")
    cadena = cadena.replace(" ","").lower()
    if cadena == cadena[::-1]:
        return jsonify({"mensaje": f"{cadena} es un palíndromo."})
    else:
        return jsonify({"mensaje": f"{cadena} no es un palíndromo."})

@app.route("/contar", methods = ["GET"])
def contar():
    cadena = request.args.get("cadena")
    vocal = request.args.get('vocal')
    cadena = cadena.lower()
    contador = sum(1 for caracter in cadena if caracter in vocal)
    return jsonify({"mensaje": f"La cadena contiene {contador} vocales con la vocal {vocal}."})


if __name__ == "__main__":
    app.run()