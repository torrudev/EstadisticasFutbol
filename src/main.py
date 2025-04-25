###
# Script principal para ejecutar todo el flujo
###

###
# Códigos de las ligas top europeas
#   -Premier League: 'PL'
#   -La Liga: 'PD'
#   -Bundesliga: 'BL1'
#   -Serie A: 'SA'
#   -Ligue 1: 'FL1'
###

from api.football_data_org import obtener_goleadores_temporada
from storage.csv_writer import guardar_estadisticas_csv

ligas = [
    {
        'id_liga': 'PL',
        'texto': 'Premier_League'
    },
    {
        'id_liga': 'PD',
        'texto': 'La_Liga'
    },
    {
        'id_liga': 'BL1',
        'texto': 'Bundesliga'
    },
    {
        'id_liga': 'SA',
        'texto': 'Serie_A'
    },
    {
        'id_liga': 'FL1',
        'texto': 'Ligue_1'
    }
]

for liga in ligas:
    id_liga = liga['id_liga']
    texto = liga['texto']
    temporada = 2023
    
    goleadores = obtener_goleadores_temporada(id_liga, temporada)
    nombre_csv = f'data/Estadisticas_{texto}{temporada}_{temporada+1}.csv'
    guardar_estadisticas_csv(goleadores, nombre_csv)
    print("csv creado")