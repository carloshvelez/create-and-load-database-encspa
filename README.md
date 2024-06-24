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

4. Descarga los archivos csv desde la [página de microdatos de la ENCSPA 2019 del dane](https://microdatos.dane.gov.co/index.php/catalog/680) y guárdalos, con el nombre que vienen, en la carpeta csv_data. Esto debe hacerse así porque los términos del DANE no permiten que comparta esos archivos por este medio, y no es posible automatizar la descarga debido al uso de captchas en esa página web. 
   
## Uso

Una vez instalado, únicamente se debe ejecutar el archivo `main.py`
```sh
    python main.py
   ```

## Referencias: 
La fuente de microdatos para la Encuesta Nacional de Consumo de SPA - 2019 es la siguiente: 

    Departamento Administrativo Nacional de Estadística [DANE]. (2020). Encuesta Nacional de Consumo de Sustancias Psicoactivas en Población General - ENCSPA- 2019. *Microdatos* [Sitio Web]. Accedido el 10/06/2024. https://microdatos.dane.gov.co/index.php/catalog/680






<br>
<br>
<br>
<br>
English
<br>
<br>
<br>
<br>


# SQLite Data Loading Application

This application enables the creation of tables and data loading into an SQLite database using CSV files downloaded from the National Statistics Department (DANE) website.

## Description

The workflow of the application is as follows:

1. **Download Dictionaries**: JSON data dictionaries are downloaded from the DANE website.
2. **Reduce Dictionaries**: The downloaded dictionaries contain redundant information, which is reduced to simplify their use.
3. **Create Tables**: Tables are created in an SQLite database using the reduced dictionaries.
4. **Load Data**: CSV files are loaded into the corresponding tables of the database.

## Project Structure

<pre>
app/
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
└── categorias.py
</pre>


## Installation

1. Clone the repository to your local machine:
    ```sh
    git clone https://github.com/your-username/your-repository.git
    cd your-repository
    ```

2. Create and activate a virtual environment (optional but recommended):
    ```sh
    python -m venv venv
    source venv/bin/activate   # On Linux/Mac
    .\venv\Scripts\activate    # On Windows
    ```

3. Install necessary dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Download the CSV files from the [DANE ENCSPA 2019 microdata page](https://microdatos.dane.gov.co/index.php/catalog/680) and save them with their original names in the `csv_data` folder. This is necessary due to DANE's terms not allowing sharing of these files through this medium, and the download cannot be automated due to CAPTCHA usage on their website.

## Usage

Once installed, simply execute the `main.py` file:
```sh
    python main.py
   ```

## References

The source of microdata for the National Survey of Psychoactive Substance Use in General Population - 2019 is as follows:

    Departamento Administrativo Nacional de Estadística [DANE]. (2020). National Survey of Psychoactive Substance Use in General Population - ENCSPA-2019. *Microdata* [Website]. Accessed 10/06/2024. https://microdatos.dane.gov.co/index.php/catalog/680
