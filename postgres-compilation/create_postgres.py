import psycopg2
import json
from os import listdir
from os.path import isfile, join

# Establecer la conexión a la base de datos
conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="obregonw2023"
)

# Obtener una instancia del cursor
cursor = conn.cursor()

# Directorio que contiene los archivos JSON
directorio = "ruta_directorio"

# Obtener la lista de archivos JSON en el directorio
archivos = [f for f in listdir(directorio) if isfile(join(directorio, f)) and f.endswith(".json")]

# Recorrer los archivos y cargar los datos en la tabla
for archivo in archivos:
    with open(join(directorio, archivo)) as f:
        data = json.load(f)
        cursor.execute("INSERT INTO datos_json (json_data) VALUES (%s)", [json.dumps(data)])

# Confirmar los cambios
conn.commit()

# Cerrar la conexión
cursor.close()
conn.close()
