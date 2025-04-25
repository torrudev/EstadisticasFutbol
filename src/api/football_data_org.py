###
# Funciones para llamar a la API(football-data.org) y obtener datos
###

import requests
import csv
import os
from dotenv import load_dotenv

# Cargar las variables del archivo .env
load_dotenv()
API_KEY = os.getenv("API_KEY")

URL_BASE = 'http://api.football-data.org/v4/'

headers = {
    "X-Auth-Token": API_KEY
}

def obtener_goleadores_temporada(id_liga, temporada):
    url = f'{URL_BASE}competitions/{id_liga}/scorers?season={temporada}&limit=400'

    # Realizar la solicitud a la API
    respuesta = requests.get(url, headers=headers)
    data = respuesta.json()

    if respuesta.status_code != 200:
        print(f"Error: {respuesta.status_code} - {data['message']}")
        return []

    # lista para guardar estadísticas de jugadores
    estadisticas_jugadores = []
    anotadores = data['scorers']

    for anotador in anotadores:
        jugador = anotador['player']

        if  anotador['goals'] is not None and anotador['goals'] > 0 or anotador['assists'] is not None and anotador['assists'] > 0:
            # Rellenar lista de estadísticas de jugadores
            estadisticas_jugadores.append(
                {
                    'id_jugador': jugador['id'],
                    'nombre_jugador': jugador['name'],
                    'goles': anotador['goals'],
                    'asistencias': anotador['assists'] or 0,
                    'penaltis': anotador['penalties'] or 0
                }
            )
    
    estadisticas_jugadores.sort(key=lambda x: (x['goles'], x['asistencias']), reverse=True)

    return estadisticas_jugadores