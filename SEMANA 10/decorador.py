from functools import wraps

# Define un decorador que imprime un mensaje antes
# y después de llamar a la función decorada
# Usando wraps para mantener los metadatos de la función original
def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Antes de llamar a la funcion")
        result = func(*args, **kwargs)
        print("Despues de llamar a la funcion")
        return result
    return wrapper

#Aplica el decorador a una Funcion
@my_decorator
def greet(name):
    """Funcion para saludar a alguien"""
    print(f"hola, {name}!")

#Llama a la funcion decorada
greet("Brayan")

#Accede a los metadatos de la funcion original
print(greet.__name__)
#Output: greet
print(greet.__doc__)
#Output: Funcion para saludar a alguien