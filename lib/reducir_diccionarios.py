import json

def reducir_diccionarios():
    """Reduce el diccionario de datos a cuatro subcategorías para cada variable"""
    archivo = "json_data/base_variables.json"

    #Abrir archivo Json
    with open(archivo, "r", encoding="utf-8") as archivo:
        data = json.load(archivo)


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




    #guardar nuevo archivo
    nombre_nuevo_archivo = "json_data/json_limpio.json"
    with open(nombre_nuevo_archivo, "w", encoding="utf-8") as archivo:
        json.dump(data, archivo, ensure_ascii=False, indent=4)
