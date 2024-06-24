import requests
import json



def obtener_diccionarios():
    """Descarga diccionario de datos para la ENCSPA desde la url especificada dentro de la función"""
    
    #Definir url de descarga
    url_base = "https://microdatos.dane.gov.co/index.php/metadata/export_variable/680/V{variable}/json"

    # Orden de las categorías en la web:
    categorias = [
            "caracteristicas", 
            "embarazo", 
            "trabajo",
            "demanda_tratamiento",
            "personas_seleccionadas",
            "personas",
            "otras_sustancias",
            "heroína",
            "extasis",
            "basuco",
            "cocaina",
            "marihuana",
            "inhalables",
            "estimulantes",
            "tranquilizantes",
            "ilegales",
            "alcohol",
            "encuestas",
            "tabaco",
            "caracteristicas_adicionales",       
        ]


    # Diccionario vacío para agrupar las variables de cada categoría
    grupo_variables = {}

    #Diccionario vacío para guardar variables descargadas
    base_variables = {}

    #Para iterar en categorías
    indice_catetogoria = 0

    for num_variable in range(38, 663):
        url = url_base.format(variable=num_variable)
        response = requests.get(url)

        if response.status_code == 200:
            
            #Cargar datos de cada variable
            datos_variable = json.loads(response.content.decode('utf-8'))        
            #Guardar cada variable en el grupo
            grupo_variables[datos_variable["name"]] = datos_variable
            print(f"Variable {datos_variable['name']} descargada con éxito")

            #La variable "Orden" señala que se inicia una nueva categoría, excepto en los casos FEX_c, PER_SELECCIONADA Y RECO_DIC
            
            if datos_variable["name"] in ["FEX_C", "PER_SELECCIONADA", "RECO_DIC"]:
                base_variables[categorias[indice_catetogoria]] = grupo_variables
                #Reiniciar diccionario de grupo de variables
                grupo_variables = dict()
                print(f"Se creó la categoría {categorias[indice_catetogoria]}")
                indice_catetogoria +=1            
            
            
            elif datos_variable["name"] == "ORDEN" and categorias[indice_catetogoria] not in ["personas", "personas_seleccionadas", "encuestas"]:
                base_variables[categorias[indice_catetogoria]] = grupo_variables
                #Reiniciar diccionario de grupo de variables
                grupo_variables = dict()
                print(f"Se creó la categoría {categorias[indice_catetogoria]}")
                indice_catetogoria +=1
    
        else:
            print(f"error descargando {url}")
        


    #Guardar diccionario de variables en archivo
    nombre_archivo = "json_data/base_variables.json"
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        json.dump(base_variables, archivo, ensure_ascii=False, indent=4)

    print("Operación finalizada")
    return 1