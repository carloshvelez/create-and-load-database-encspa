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

una vez instalado, únicamente se debe ejecutar el archivo `main.py`
```sh
    python main.py
    ```