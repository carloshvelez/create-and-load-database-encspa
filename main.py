from lib import cargar_datos, crear_tablas, obtener_diccionarios, reducir_diccionarios
import utils.categorias as categorias

def main():
    obtener_diccionarios.obtener_diccionarios()
    reducir_diccionarios.reducir_diccionarios()
    crear_tablas.crear_tablas()


    for nombre_tabla, nombre_archivo in categorias.categorias.items():
        cargar_datos.cargar_datos(nombre_archivo, nombre_tabla)
    print("Trabajo realizado con éxito. Ahora puede usar los microdatos y la base de datos")


if __name__ == "__main__":
    main()