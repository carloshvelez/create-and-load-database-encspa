# Crear script sql de creación de tabla para cada grupo en el archivo JSON
def generar_script_crear_tabla(nombre, grupo):
    """Genera un escript para crear una tabla en sqlite3. El parámetro nombre define el nombre de la tabla y el parámetro grupo define el nombre de las columnas"""
    
    print(f"Generando script de creación para la tabla {nombre}\n...\n...\n")
    cadena_create = f'CREATE TABLE IF NOT EXISTS {nombre}('
    cadena_campos = []
    for nombre, campos in grupo.items():

        # Configurar nombre para cada campo en la tabla       
        nombre_campo = nombre

        # Configurar el tipo de variable para cada campo
        if nombre=="Depmuni":            
            tipo_variable = "TEXT" 
        elif campos["intervalo"] == "discrete":
            tipo_variable = "INTEGER"        
        else:
            tipo_variable = "FLOAT"
        
        cadena_campos.append(" ".join(["   ",nombre_campo, tipo_variable, ",\n"]))

    primary_key = f'"id" INTEGER PRIMARY KEY AUTOINCREMENT,'
    
    # Configurar relaciones con "DIRECTORIO"
    foreign_key = ""
    if nombre != "personas":
        foreign_key = 'FOREIGN KEY ("DIRECTORIO") REFERENCES "personas"("DIRECTORIO")'

    # Devolver cadena concatenada.
    print(f"Script de creación para la tabla {nombre} generado con éxito")
    return f'{cadena_create}\n{"".join(cadena_campos)}    {primary_key}\n    {foreign_key}\n );\n' 