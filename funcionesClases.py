from datos import socios, clases, instructores
from funcionesValidacion import *
import json
#--------------------- Funciones relacionadas a la entidad Clases ------------------------
"""
craerClases recibe por parametro la lista de diccionarios 'clases', crea en la funcion un diccionario nuevo para luego 
hacer un append en la lista de diccionarios 'clases'
"""
def crearClases(archivo):
    print("\n=== Crear Clase ===")
    try:
        with open(archivo, 'r', encoding="UTF-8") as datos:
            clases = json.load(datos)
        
        if clases:
            id_clase = max(clase["IdClase"] for clase in clases) + 1
        else:
            id_clase = 1
    
        nombreClase = input("Ingrese el nombre de la clase: ")
        dia, hora=esClaseDisponible(archivo)
        idInstructor = input("Ingrese el ID del instructor: ")

        nuevo = {
            "IdClase": id_clase,
            "NombreClase": nombreClase,
            "Dia": dia,
            "Hora": hora,
            "IdInstructor": idInstructor,
            "Activo": "Activo"
        }

        clases.append(nuevo)
        with open(archivo, 'w', encoding="UTF-8") as datos:
            json.dump(clases, datos, ensure_ascii=False)
        print("Se agrego la clase con exito")
    
    except (FileNotFoundError, OSError) as error:
        print(f'Error! {error}')

"""
darBajaClase recibe por parametros la lista de diccionarios 'listaClases' y el id de la clase a dar de baja (pedido previamente en el main) y cambia 
el campo [Activo] a "Inactivo"
"""
def darBajaClase(listaClases, idClase):
    for clase in listaClases:
        clase_validada = validarClase(listaClases, idClase)
        if clase_validada == True:
            clase["Activo"] = "Inactivo"
            return f"Clase {clase['NombreClase']} dada de baja."
    print("Clase no encontrada o inactiva")

"""darAltaClase recibe por parametros la lista de diccionarios 'listaClases' y el id de la clase a dar de alta (pedido previamente en el main) y cambia 
el campo [Activo] a "Activo" """
def darAltaClase(listaClases, idClase):
    for clase in listaClases:
        clase_validada = validarClase(listaClases, idClase)
        if clase_validada == False:
            clase["Activo"] = "Activo"
            return f"Clase {clase['NombreClase']} dada de alta."
    print("Clase no encontrada o activa")

"""
mostrarClases recibe por parametro la lista de diccionarios 'clases' y printea por orden de legajo la lista completa de clases, tanto
inactivos como activos
"""
def mostrarClases(archivo):
    clear()
    try:
        with open(archivo, 'r', encoding="UTF-8") as datos:
            clases = json.load(datos)
            encabezados = ["IdClase", "NombreClase", "Dia", "Hora", "IdInstructor", "Activo"]
            print(" | ".join([e.center(15) for e in encabezados]))
            print("-" * (len(encabezados) * 18))

            for clase in clases:
                if clase["Activo"] == "Activo":
                    fila = [
                        str(clase["IdClase"]).center(15),
                        clase["NombreClase"].center(15),
                        clase["Dia"].center(15),
                        clase["Hora"].center(15),
                        str(clase["IdInstructor"]).center(15),
                        clase["Activo"].center(15)
                    ]
                    print(" | ".join(fila))

            input('Presione una tecla para continuar...')

    except (FileNotFoundError, OSError) as error:
        print(f'Error! {error}')

"""
editarClases recibe por parametro la lista de diccionarios 'clases' y el id de la clase a modificar. luego pregunta que campo del diccionario
se quiere editar. solo se pueden editar clases en estado 'Activo'
"""
def editarClases(listaClases, idClase):
    clear()
    print("\n=== Editar Clase ===")
    print("1. Nombre")
    print("2. Día")
    print("3. Hora")
    print("4. Instructor")
    print("0. Salir")
    campo = int(input("Ingrese el campo a modificar: "))

    clase_encontrada = False

    for clase in listaClases:
        if clase["IdClase"] == str(idClase) and clase["Activo"] == "Activo":
            clase_encontrada = True

            if campo == 1:
                nombreClase = input("Ingrese el nuevo nombre de la clase: ")
                clase["NombreClase"] = nombreClase
                print("Nombre modificado con éxito.")

            elif campo == 2:
                dia = input("Ingrese el nuevo día: ")
                clase["Dia"] = dia
                print("Día modificado con éxito.")

            elif campo == 3:
                hora = input("Ingrese la nueva hora: ")
                clase["Hora"] = hora
                print("Hora modificada con éxito.")

            elif campo == 4:
                idInstructor = input("Ingrese el nuevo ID del instructor: ")
                clase["IdInstructor"] = idInstructor
                print("Instructor modificado con éxito.")

            elif campo == 0:
                print("Saliendo de la edición.")
            else:
                print("Campo inválido.")

            input("Presione una tecla para continuar...")
            break

    if not clase_encontrada:
        print("Clase no encontrada o inactiva.")
        input("Presione una tecla para continuar...")
