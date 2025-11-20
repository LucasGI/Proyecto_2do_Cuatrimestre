from funcionesValidacion import *
from menus import *
import json
import re 

#--------------------- Funciones relacionadas a la entidad Instructores ------------------------
"""
crearInstryctor recibe por parametro la lista de diccionarios 'instructores', crea en la funcion un diccionario nuevo para luego 
hacer un append en la lista de diccionarios 'instructores'
"""
def crearInstructor(archivo):
    print("\n=== Crear Instructor ===")
    try:
        with open(archivo, 'r', encoding="UTF-8") as datos:
            instructores = json.load(datos)
        
    

        id_instructor = len(instructores) + 1
        nombre = validarNombre()
        apellido=validarApellido()
        fechaNac = validarFecha()

        nuevo = {
            "IdInstructor": id_instructor,
            "Nombre": nombre,
            "Apellido": apellido,
            "FechaNac": fechaNac,
            "Activo": "Activo"
        }

        instructores.append(nuevo)
        with open(archivo, 'w', encoding="UTF-8") as datos:
            json.dump(instructores, datos, ensure_ascii=False)

        print("Instructor agregado con éxito.")
        input("Presione Enter para continuar...")

    except (FileNotFoundError, OSError) as error:
        print(f'Error! {error}')
        input("Presione una tecla para continuar.")

"""
darBajaClase recibe por parametros la lista de diccionarios 'listaClases' y el id de la clase a dar de baja (pedido previamente en el main) y cambia 
el campo [Activo] a "Inactivo"
"""
def darBajaInstructor(archivo, idInstructor):
    try:
        with open(archivo, 'r', encoding="UTF-8") as datos:
            instructores = json.load(datos)
        
        instructor_validado = validarInstructor(instructores, idInstructor)
        if not instructor_validado:
            print(f"El instructor con ID {idInstructor} ya está inactivo.")
        else:
            encontrado = False
            for instructor in instructores:
                if instructor["IdInstructor"] == idInstructor:
                    instructor["Activo"] = re.sub("Activo", "Inactivo", instructor["Activo"])
                    print(f"instructor {instructor['Nombre']} dado de baja.")
                    encontrado = True
                    break

            if not encontrado:
                print(f"No se encontró ningun instructor con el ID {idInstructor}.")

        with open(archivo, 'w', encoding="UTF-8") as datos:
            json.dump(instructores, datos, ensure_ascii=False, indent=4)

        input('Presione una tecla para continuar...')

    except (FileNotFoundError, OSError) as error:
        print(f'Error! {error}')
        input("Presione una tecla para continuar.")

"""
darAltaClase recibe por parametros la lista de diccionarios 'listaClases' y el id de la clase a dar de alta (pedido previamente en el main) y cambia 
el campo [Activo] a "Inactivo"
"""
def darAltaInstructor(archivo, idInstructor):
    try:
        with open(archivo, 'r', encoding="UTF-8") as datos:
            instructores = json.load(datos)
        
        instructor_validado = validarInstructor(instructores, idInstructor)
        if instructor_validado:
            print(f"El instructor con ID {idInstructor} ya está activo.")
        else:
            encontrado = False
            for instructor in instructores:
                if instructor["IdInstructor"] == idInstructor:
                    instructor["Activo"] = re.sub("Inactivo", "Activo", instructor["Activo"])
                    print(f"instructor {instructor['Nombre']} dado de alta.")
                    encontrado = True
                    break

            if not encontrado:
                print(f"No se encontró ningun instructor con el ID {idInstructor}.")

        with open(archivo, 'w', encoding="UTF-8") as datos:
            json.dump(instructores, datos, ensure_ascii=False, indent=4)

        input('Presione una tecla para continuar...')

    except (FileNotFoundError, OSError) as error:
        print(f'Error! {error}')
        input("Presione una tecla para continuar.")

"""
mostrarInstructores recibe por parametro la lista de diccionarios 'instructores' y printea por orden de legajo la lista completa de instructores,solo activos
"""
def mostrarInstructores(archivo):
    clear()
    try:
        with open(archivo, 'r', encoding="UTF-8") as datos:
            instructores = json.load(datos)
        
        encabezados = ["IdInstructor", "Nombre", "Apellido", "FechaNac", "Activo"]
        print(" | ".join([e.center(15) for e in encabezados]))
        print("-" * (len(encabezados) * 18))

        for instructor in instructores:
            if instructor["Activo"] in ["Activo"]:
                fila = [
                    str(instructor["IdInstructor"]),
                    instructor["Nombre"],
                    instructor["Apellido"],
                    instructor["FechaNac"],
                    instructor["Activo"]
                ]
                print(" | ".join([dato.center(15) for dato in fila]))

        input("Presione una tecla para continuar...")
    
    except (FileNotFoundError, OSError) as error:
        print(f'Error! {error}')
        input("Presione una tecla para continuar.")

"""
editarInstructores recibe por parametro la lista de diccionarios 'instructores' y el id del instructor a modificar. luego pregunta que campo del diccionario
se quiere editar. solo se pueden editar instructores en estado 'Activo'
"""
def editarInstructor(archivo, idInstructor):
    clear()

    try:
        with open(archivo, 'r', encoding="UTF-8") as datos:
            instructores = json.load(datos)

        if not validarInstructor(instructores, idInstructor):
            print("Instructor no encontrado o inactivo")
            input("Presione una tecla para continuar...")
            return
        
        for instructor in instructores:
            if instructor["IdInstructor"] == idInstructor:

                print("\n=== Editar Instructor ===")
                print("1. Nombre")
                print("2. Apellido")
                print("3. Fecha de Nacimiento")
                print("4. Salir")
                while True:
                    try:
                        campo = int(input("Ingrese el campo a modificar: "))
                        break
                    except ValueError:
                        print("Error, Ingrese una opcion numerica: ")
                if campo == 1:
                    nombre = validarNombre()
                    instructor["Nombre"] = nombre
                    print("Nombre modificado con éxito.")
                elif campo == 2:
                    apellido=validarApellido()
                    instructor["Apellido"] = apellido
                    print("Apellido modificado con éxito.")
                elif campo == 3:
                    fechaNac=validarFecha()
                    instructor["FechaNac"] = fechaNac
                    print("Fecha de nacimiento modificada con éxito.")

                elif campo == 4:
                    print("Saliendo de la edición.")
                else:
                    print("Campo inválido.")

                with open(archivo, 'w', encoding="UTF-8") as datos:
                    json.dump(instructores, datos, ensure_ascii=False, indent=4)

                input("Presione una tecla para continuar...")
                break



    except (FileNotFoundError, OSError) as error:
        print(f'Error {error}')
        input('Presione una tecla para continuar...')



def mostrarInstructoresOrdenado(archivo, instructores=None, indice=0):
    # Si instructores es None, significa que es la primera llamada (leer archivo)
    if instructores is None:
        clear()
        try:
            with open(archivo, 'r', encoding="UTF-8") as datos:
                instructores = json.load(datos)

            # Filtrar solo activos y ordenar
            instructores = [i for i in instructores if i["Activo"] == "Activo"]
            instructores.sort(key=lambda x: x["Apellido"])

            encabezados = ["IdInstructor", "Nombre", "Apellido", "FechaNac", "Activo"]
            print(" | ".join([e.center(15) for e in encabezados]))
            print("-" * (len(encabezados) * 18))

            # Llamada inicial a la recursión
            mostrarInstructoresOrdenado(archivo, instructores, 0)

            input("\nPresione una tecla para continuar...")

        except (FileNotFoundError, OSError) as error:
            print(f"Error! {error}")
            input("Presione una tecla para continuar...")

    else:
        # Caso base: si ya mostramos todos los instructores, terminamos
        if indice >= len(instructores):
            return
        
        # Mostrar el instructor actual
        instructor = instructores[indice]
        fila = [
            str(instructor["IdInstructor"]),
            instructor["Nombre"],
            instructor["Apellido"],
            instructor["FechaNac"],
            instructor["Activo"]
        ]
        print(" | ".join([dato.center(15) for dato in fila]))
        # Llamada recursiva para el siguiente
        mostrarInstructoresOrdenado(archivo, instructores, indice + 1)

mostrarInstructoresOrdenado("archivos/instructores.json")