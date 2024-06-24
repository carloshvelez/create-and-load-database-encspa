import sqlite3
import pandas as pd


def cargar_datos(nombre_archivo, nombre_tabla, folder="csv_data"):
    """Toma los datos del archivo csv especificado en los parámetros y carga los datos a la tabla correspondiente"""
    
    archivo = folder + "/" + nombre_archivo
    #evitar la transformación de código municipio a texto
    if nombre_tabla == "encuestas":
        df =  pd.read_csv(archivo, dtype={'Depmuni': str})
        df["Depmuni"]= df["Depmuni"].astype(str)        
    else:
        df = pd.read_csv(archivo)
    conexion = sqlite3.connect("database/encspa.db")
    cursor = conexion.cursor()

    df.to_sql(nombre_tabla, conexion, if_exists='append', index=False)
    conexion.commit()
    conexion.close()
    print(f"Carga de datos exitosa para la tabla {nombre_tabla}")
    return 1
