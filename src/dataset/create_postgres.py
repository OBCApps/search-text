import json
import csv

# Abre el archivo JSON
with open('data_elecciones/tweets_2018-08-07.json', encoding='utf-8') as file:
    data = json.load(file)

# Abre un archivo CSV para escribir los datos
with open('archivo.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)

    # Escribe los encabezados de las columnas
    writer.writerow(data[0].keys())

    # Escribe cada fila de datos
    for row in data:
        writer.writerow(row.values())