from datos import socios, clases, instructores
from funcionesValidacion import *
import json
#--------------------- Funciones relacionadas a la entidad Clases ------------------------




def crearClases(archivo):
    """
    craerClases recibe por parametro la lista de diccionarios 'clases', crea en la funcion un diccionario nuevo para luego 
    hacer un append en la lista de diccionarios 'clases'
    """
    print("\n=== Crear Clase ===")
    try:
        with open(archivo, 'r', encoding="UTF-8") as datos:
            clases = json.load(datos)
        
        
        id_clase = len(clases) + 1
        nombreClase = validarOpcion("Ingrese el nombre de la clase: ", ["Musculacion", "Spinning", "Zumba", "Funcional", "Pilates"])
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
        input('Presione una tecla para continuar...')
    
    except (FileNotFoundError, OSError) as error:
        print(f'Error! {error}')
        input('Presione una tecla para continuar...')





def darBajaClase(archivo, idClase):
    """
    darBajaClase recibe por parametros la lista de diccionarios 'listaClases' y el id de la clase a dar de baja (pedido previamente en el main) y cambia 
    el campo [Activo] a "Inactivo"
    """
    try:
        with open(archivo, 'r', encoding="UTF-8") as datos:
            clases = json.load(datos)

        clase_validada = validarClase(clases, idClase)
        if not clase_validada:
            print(f"La clase con ID {idClase} ya está inactiva o no existe.")
        else:
            encontrada = False
            for clase in clases:
                if clase["IdClase"] == idClase:
                    clase["Activo"] = re.sub("Activo", "Inactivo", clase["Activo"])
                    print(f"Clase {clase['NombreClase']} dada de baja.")
                    encontrada = True
                    break

            if not encontrada:
                print(f"No se encontró ninguna clase con el ID {idClase}.")

        with open(archivo, 'w', encoding="UTF-8") as datos:
            json.dump(clases, datos, ensure_ascii=False, indent=4)

        input('Presione una tecla para continuar...')

    except (FileNotFoundError, OSError) as error:
        print(f'Error! {error}')
        input('Presione una tecla para continuar...')





def darAltaClase(archivo, idClase):
    """darAltaClase recibe por parametros la lista de diccionarios 'listaClases' y el id de la clase a dar de alta (pedido previamente en el main) y cambia 
    el campo [Activo] a "Activo" """
    try:
        with open(archivo, 'r', encoding="UTF-8") as datos:
            clases = json.load(datos)

        
        clase_validada = validarClase(clases, idClase)
        if clase_validada:
            print(f"La clase con ID {idClase} ya está activa.")
        else:
            encontrada = False
            for clase in clases:
                if clase["IdClase"] == idClase:
                    clase["Activo"] = re.sub("Inactivo", "Activo", clase["Activo"])
                    print(f"Clase {clase['NombreClase']} dada de alta.")
                    encontrada = True
                    break  

            if not encontrada:
                print(f"No se encontró ninguna clase con el ID {idClase}.")

        with open(archivo, 'w', encoding="UTF-8") as datos:
            json.dump(clases, datos, ensure_ascii=False, indent=4)

        input('Presione una tecla para continuar...')

    except (FileNotFoundError, OSError) as error:
        print(f'Error! {error}')
        input('Presione una tecla para continuar...')



def mostrarClases(archivo):
    """
    mostrarClases recibe por parametro la lista de diccionarios 'clases' y printea por orden de legajo la lista completa de clases, tanto
    inactivos como activos
    """
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




def editarClases(archivo, idClase):
    """
    editarClases recibe por parametro la lista de diccionarios 'clases' y el id de la clase a modificar. luego pregunta que campo del diccionario
    se quiere editar. solo se pueden editar clases en estado 'Activo'
    """
    clear()
    print("\n=== Editar Clase ===")
    print("1. Nombre")
    print("2. Día")
    print("3. Hora")
    print("4. Instructor")
    print("0. Salir")
    while True:
        try:
            campo = int(input("Ingrese el campo a modificar: "))
            break
        except ValueError:
            print("Error, Debe ingresar un entero")

    try:
        with open(archivo, 'r', encoding="UTF-8") as datos:
            clases = json.load(datos)

        clase_encontrada = False
        for clase in clases:
            if clase["IdClase"] == idClase and clase["Activo"].strip().lower() == "activo":
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

                with open(archivo, 'w', encoding="UTF-8") as datos:
                    json.dump(clases, datos, ensure_ascii=False)

                input("Presione una tecla para continuar...")
                break

        if clase_encontrada == False:
            print("Clase no encontrada o inactiva.")
            input("Presione una tecla para continuar...")
        
    except (FileNotFoundError, OSError) as error:
        print(f'Error {error}')
        input('Presione una tecla para continuar...')


def ordenarClasesPorHora(archivo, orden):
    try:
        with open(archivo, 'r', encoding='UTF-8') as datos:
            clases = json.load(datos)

        clases.sort(key = lambda h: h["Hora"], reverse=orden)

        print("\n=== Clases Ordenadas Por Horario ===")
        encabezados = ["IdClase", "NombreClase", "Dia", "Hora", "IdInstructor", "Activo"]
        print(" | ".join([e.center(15) for e in encabezados]))
        print("-"*(len(encabezados)*18))

        for clase in clases:
            if clase["Activo"].strip().lower() == "activo":
                fila = [
                    str(clase["IdClase"]).center(15),
                    clase["NombreClase"].center(15),
                    clase["Dia"].center(15),
                    clase[("Hora")].center(15),
                    str(clase["IdInstructor"]).center(15),
                    clase["Activo"].center(15)
                ]
                print(" | ".join(fila))

        input("Presione una tecla pa continuar... ")


    except(FileNotFoundError, OSError) as error:
        print(f"error al abrir archivo {error}")
        input("presione una tecla para continuar: ")


