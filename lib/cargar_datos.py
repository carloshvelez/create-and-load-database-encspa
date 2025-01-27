import sqlite3
import pandas as pd
import os


def cargar_datos(nombre_archivo, nombre_tabla, folder="csv_data"):
    """Toma los datos del archivo csv especificado en los parámetros y carga los datos a la tabla correspondiente"""
    
    # Crear directorio csv_data si no existe
    os.makedirs(folder, exist_ok=True)
    
    archivo = folder + "/" + nombre_archivo
    if not os.path.exists(archivo):
        raise FileNotFoundError(f"El archivo {archivo} no existe. Por favor, asegúrese de que los archivos CSV necesarios estén en el directorio {folder}/\nPor favor recuerde que para que este Script funcione, usted debe descargar y descomprimir manualmente los archivos descargados desde la web https://microdatos.dane.gov.co/index.php/catalog/680/get_microdata")
    
    #evitar la transformación de código municipio a texto
    if nombre_tabla == "encuestas":
        df =  pd.read_csv(archivo, dtype={'Depmuni': str})
        df["Depmuni"]= df["Depmuni"].astype(str)        
    else:
        df = pd.read_csv(archivo)

    conexion = sqlite3.connect("database/encspa.db")
    cursor = conexion.cursor()

    # Get the columns of the target table
    cursor.execute(f"PRAGMA table_info({nombre_tabla})")
    table_columns = [column[1] for column in cursor.fetchall()]

    # Filter DataFrame to only include columns that exist in the target table
    df = df[[col for col in df.columns if col in table_columns]]

    df.to_sql(nombre_tabla, conexion, if_exists='append', index=False)
    conexion.commit()
    conexion.close()
    print(f"Carga de datos exitosa para la tabla {nombre_tabla}")
    return 1
