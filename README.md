# Aplicación de Carga de Datos a SQLite

Esta aplicación permite crear tablas y cargar datos en una base de datos SQLite utilizando archivos CSV descargados desde la página web del Departamento Nacional de Estadística (DANE). 

## Descripción

El flujo de trabajo de la aplicación es el siguiente:

1. **Descargar Diccionarios**: Se descargan diccionarios de datos en formato JSON desde el sitio web del DANE.
2. **Reducir Diccionarios**: Los diccionarios descargados contienen información redundante, por lo que se reducen para facilitar su uso.
3. **Crear Tablas**: Se crean las tablas en una base de datos SQLite utilizando los diccionarios reducidos.
4. **Cargar Datos**: Los archivos CSV se cargan en las tablas correspondientes de la base de datos.

## Estructura del Proyecto

<pre>app/
├── main.py
├── csv_data/
├── database/
├── json_data/
├── lib/
│ ├── init.py
│ ├── crear_tablas.py
│ ├── importar_datos_bd.py
│ ├── obtener_diccionarios.py
│ └── reducir_diccionarios.py
└── utils/
   ├── categorias.py
</pre>


## Instalación

1. Clona el repositorio en tu máquina local:
    ```sh
    git clone https://github.com/tu-usuario/tu-repositorio.git
    cd tu-repositorio
    ```

2. Crea y activa un entorno virtual (opcional pero recomendado):
    ```sh
    python -m venv venv
    source venv/bin/activate   # En Linux/Mac
    .\venv\Scripts\activate    # En Windows
    ```

3. Instala las dependencias necesarias:
    ```sh
    pip install -r requirements.txt
    ```

4. Descarga los archivos csv desde la [página de microdato de la ENCSPA 2019 del dane](https://microdatos.dane.gov.co/index.php/catalog/680) y guárdalos, con el nombre que vienen, en la carpeta csv_data. Esto debe hacerse así porque los términos del DANE no permiten que comparta esos archivos por este medio, y no es posible automatizar la descarga debido al uso de captchas en esa página web. 
   
## Uso

1. **Descargar Diccionarios**:
    La función `obtener_diccionarios()` descarga los diccionarios de datos desde el enlace del DANE y los guarda en la carpeta especificada.
    ```python
    from lib.obtener_diccionarios import obtener_diccionarios

    obtener_diccionarios()
    ```

2. **Reducir Diccionarios**:
    La función `reducir_diccionarios()` procesa los diccionarios descargados para eliminar información redundante.
    ```python
    from lib.reducir_diccionarios import reducir_diccionarios

    reducir_diccionarios()
    ```

3. **Crear Tablas**:
    La función `crear_tablas()` crea las tablas en la base de datos SQLite utilizando los diccionarios reducidos.
    ```python
    from lib.crear_tablas import crear_tablas

    crear_tablas()
    ```

4. **Cargar Datos**:
    Los archivos CSV se cargan en las tablas de la base de datos utilizando la función `importar_tabla_bd()` para cada archivo y tabla.
    ```python
    from lib.importar_datos_bd import importar_tabla_bd
    import utils.categorias as categorias

    for nombre_tabla, nombre_archivo in categorias.categorias.items():
        importar_tabla_bd(nombre_archivo, nombre_tabla)
    ```

5. **Ejecutar el Flujo Completo**:
    Puedes ejecutar todas las funciones anteriores en el orden correcto llamando a la función `main()` en `main.py`.
    ```python
    if __name__ == "__main__":
        main()
    ```

## Ejemplo

```python
# main.py

from lib import crear_tablas, importar_datos_bd, obtener_diccionarios, reducir_diccionarios
import utils.categorias as categorias

def main():
    obtener_diccionarios.obtener_diccionarios()
    reducir_diccionarios.reducir_diccionarios()
    crear_tablas.crear_tablas()

    for nombre_tabla, nombre_archivo in categorias.categorias.items():
        importar_datos_bd.importar_tabla_bd(nombre_archivo, nombre_tabla)
    
    print("Trabajo realizado con éxito. Ahora puede usar los diccionarios y la base de datos")

if __name__ == "__main__":
    main()
