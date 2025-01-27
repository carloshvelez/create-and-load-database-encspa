import json
import logging
import os
from typing import Dict, Any

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('json_data/process.log'),
        logging.StreamHandler()
    ]
)

def reducir_diccionarios() -> int:
    """Reduce el diccionario de datos a cuatro subcategorías para cada variable"""
    archivo = "json_data/base_variables.json"

    try:
        if not os.path.exists(archivo):
            logging.error(f"El archivo {archivo} no existe")
            return 0
            
        #Abrir archivo Json
        with open(archivo, "r", encoding="utf-8") as archivo:
            data = json.load(archivo)
    except json.JSONDecodeError as e:
        logging.error(f"Error al decodificar el archivo JSON: {e}")
        return 0
    except Exception as e:
        logging.error(f"Error inesperado al leer el archivo: {e}")
        return 0


    #Para cada variable en archivo json viejo, 
    for categoria, grupo_variables in data.items(): 
        print(categoria)   
        
        for variable, campo in grupo_variables.items():   
            #print(campo["labl"])     
            variable_limpia = {
                "etiqueta": campo["labl"],
                "intervalo": campo["var_intrvl"],
                "decimales": campo["var_dcml"],
                "categorias": campo["var_catgry"]
            }       
            grupo_variables[variable] = variable_limpia
            

    data["personas_seleccionadas"]["FEX_C"] = {
            "etiqueta": "Factor de expansión",
            "intervalo": "contin",
            "decimales": "14",
            "categorias": []
        } 




    try:
        #Crear directorio si no existe
        os.makedirs("json_data", exist_ok=True)
        
        #guardar nuevo archivo
        nombre_nuevo_archivo = "json_data/json_limpio.json"
        with open(nombre_nuevo_archivo, "w", encoding="utf-8") as archivo:
            json.dump(data, archivo, ensure_ascii=False, indent=4)
        logging.info("Diccionario reducido guardado exitosamente")
        return 1
    except Exception as e:
        logging.error(f"Error al guardar el archivo: {e}")
        return 0
