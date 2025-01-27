import json
import sqlite3
import pandas as pd
import os
import json
import logging
import lib.generar_script_crear_tabla as generar_script_crear_tabla
from typing import Dict

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('database/database.log'),
        logging.StreamHandler()
    ]
)

def crear_tablas() -> int:
    """Con base en el diccionario reducido genera un escript concatenado para cada categoría/grupo variables en ese diccionario. POsteriormente ejecuta el escript en el archivo de base de datos"""

    archivo = "json_data/json_limpio.json"

    try:
        if not os.path.exists(archivo):
            logging.error(f"El archivo {archivo} no existe")
            return 0

        # Abrir archivo Json
        with open(archivo, "r", encoding="utf-8") as archivo:
            microdatos = json.load(archivo)

        # Generar un script global para todas las tablas
        scripts_concatenados = ""
        for categoria, grupo_variables in microdatos.items():
            try:
                scripts_concatenados += generar_script_crear_tabla.generar_script_crear_tabla(categoria, grupo_variables)
            except Exception as e:
                logging.error(f"Error al generar script para la categoría {categoria}: {e}")
                return 0

        # Crear directorio database si no existe
        os.makedirs("database", exist_ok=True)

        # Abrir conexión y ejecutar scripts
        try:
            conexion = sqlite3.connect("database/encspa.db")
            cursor = conexion.cursor()
            cursor.executescript(scripts_concatenados)
            conexion.commit()
            logging.info("Tablas creadas exitosamente en la base de datos")
            return 1
        except sqlite3.Error as e:
            logging.error(f"Error en la base de datos: {e}")
            return 0
        finally:
            if 'conexion' in locals():
                conexion.close()

    except json.JSONDecodeError as e:
        logging.error(f"Error al decodificar el archivo JSON: {e}")
        return 0
    except Exception as e:
        logging.error(f"Error inesperado: {e}")
        return 0

    print("Se crearon las tablas en la base de datos: database/encspa.db")

    return 1








