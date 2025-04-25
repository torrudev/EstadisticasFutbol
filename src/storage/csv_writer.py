###
# Funciones para escribir archivos CSV
###

import csv

def guardar_estadisticas_csv(jugadores, nombre_archivo):
    with open(nombre_archivo, mode='w', newline='', encoding='utf-8') as archivo_csv:
        writer = csv.DictWriter(archivo_csv, fieldnames=jugadores[0].keys())
        writer.writeheader()
        writer.writerows(jugadores)