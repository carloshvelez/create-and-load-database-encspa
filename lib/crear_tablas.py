import json
import sqlite3
import pandas as pd
import lib.generar_script_crear_tabla as generar_script_crear_tabla

def crear_tablas():
    """Con base en el diccionario reducido genera un escript concatenado para cada categoría/grupo variables en ese diccionario. POsteriormente ejecuta el escript en el archivo de base de datos"""

    archivo = "json_data/json_limpio.json"

    # Abrir archivo Json
    with open(archivo, "r", encoding="utf-8") as archivo:
        microdatos = json.load(archivo)


    # Generar un script global, que construya todas las tablas en las bd, para cada categoría de microdatos   
    scripts_concatenados = ""
    for categoria, grupo_variables in microdatos.items():
        scripts_concatenados += generar_script_crear_tabla.generar_script_crear_tabla(categoria, grupo_variables)


    # Abrir conexión
    conexion = sqlite3.connect("database/encspa.db")
    cursor = conexion.cursor()

    # Ejecutar script
    cursor.executescript(f"""{scripts_concatenados}""")
    conexion.commit()

    # Cerrar conexión.
    conexion.close()

    print("Se crearon las tablas en la base de datos: database/encspa.db")

    return 1








