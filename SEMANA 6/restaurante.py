# Importar módulo sqlite3
import sqlite3

# Crear conexión a la base de datos
conn = sqlite3.connect("restaurante.db")

# Crear tabla de carreras
conn.execute(
    """
    CREATE TABLE PLATOS
    (id INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL,
    precio INTEGER NOT NULL
    categoria TEXT NOT NULL,);
    """
)

# Consultar datos
print("CARRERAS:")
cursor = conn.execute("SELECT * FROM CARRERAS")
for row in cursor:
    print(row)

# CARRERAS:
# (1, 'Ingeniería en Informática', 5)
# (2, 'Licenciatura en Administración', 4)

conn.execute(
    """
    CREATE TABLE MESAS
    (id INTEGER PRIMARY KEY,);
    """
)

# Consultar datos
print("MESAS:")
cursor = conn.execute("SELECT * FROM CARRERAS")
for row in cursor:
    print(row)

conn.execute(
    """
    CREATE TABLE PEDIDOS
    (id INTEGER PRIMARY KEY,
    plato TEXT NOT NULL,
    mesa INTEGER NOT NULL,
    cantidad TEXT NOT NULL,
    categoria TEXT NOT NULL,);
    """
)

# Consultar datos
print("PEDIDOS:")
cursor = conn.execute("SELECT * FROM CARRERAS")
for row in cursor:
    print(row)