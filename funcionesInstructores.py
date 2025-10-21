from datos import socios, clases, instructores
from funcionesValidacion import clear, validarFecha
#--------------------- Funciones relacionadas a la entidad Instructores ------------------------
"""
crearInstryctor recibe por parametro la lista de diccionarios 'instructores', crea en la funcion un diccionario nuevo para luego 
hacer un append en la lista de diccionarios 'instructores'
"""
def crearInstructor(instructores):
    print("\n=== Crear Instructor ===")
    id_instructor = str(len(instructores) + 1)
    nombre = input("Ingrese el nombre: ")
    apellido = input("Ingrese el apellido: ")
    fechaNac = validarFecha()

    nuevo = {
        "IdInstructor": id_instructor,
        "Nombre": nombre,
        "Apellido": apellido,
        "FechaNac": fechaNac,
        "Activo": "Activo"
    }

    instructores.append(nuevo)
    print("Instructor agregado con éxito.")

"""
darBajaClase recibe por parametros la lista de diccionarios 'listaClases' y el id de la clase a dar de baja (pedido previamente en el main) y cambia 
el campo [Activo] a "Inactivo"
"""
def darBajaInstructor(listaInstructores, idInstructor):
    for instructor in listaInstructores:
        if instructor["IdInstructor"] == str(idInstructor):
            if instructor["Activo"] == "Activo":
                instructor["Activo"] = "Inactivo"
                return f"Instructor {instructor['Nombre']} {instructor['Apellido']} dado de baja."
            else:
                return f"El instructor {instructor['Nombre']} {instructor['Apellido']} ya estaba inactivo."
    print("Instructor no encontrado.")

"""
darAltaClase recibe por parametros la lista de diccionarios 'listaClases' y el id de la clase a dar de alta (pedido previamente en el main) y cambia 
el campo [Activo] a "Inactivo"
"""
def darAltaInstructor(listaInstructores, idInstructor):
    for instructor in listaInstructores:
        if instructor["IdInstructor"] == str(idInstructor):
            if instructor["Activo"] == "Inactivo":
                instructor["Activo"] = "Activo"
                return f"Instructor {instructor['Nombre']} {instructor['Apellido']} dado de alta."
            else:
                return f"El instructor {instructor['Nombre']} {instructor['Apellido']} ya estaba activo."
    print("Instructor no encontrado.")

"""
mostrarInstructores recibe por parametro la lista de diccionarios 'instructores' y printea por orden de legajo la lista completa de instructores, tanto
inactivos como activos
"""
def mostrarInstructores(instructores):
    clear()
    encabezados = ["IdInstructor", "Nombre", "Apellido", "FechaNac", "Activo"]
    print(" | ".join([e.center(15) for e in encabezados]))
    print("-" * (len(encabezados) * 18))

    for instructor in instructores:
        if instructor["Activo"] in ["Activo", "Inactivo"]:
            fila = [
                instructor["IdInstructor"],
                instructor["Nombre"],
                instructor["Apellido"],
                instructor["FechaNac"],
                instructor["Activo"]
            ]
            print(" | ".join([dato.center(15) for dato in fila]))

    input("Presione una tecla para continuar...")

"""
editarInstructores recibe por parametro la lista de diccionarios 'instructores' y el id del instructor a modificar. luego pregunta que campo del diccionario
se quiere editar. solo se pueden editar instructores en estado 'Activo'
"""
def editarInstructor(listaInstructores, idInstructor):
    clear()
    print("\n=== Editar Instructor ===")
    print("1. Nombre")
    print("2. Apellido")
    print("3. Fecha de Nacimiento")
    print("4. Salir")
    campo = int(input("Ingrese el campo a modificar: "))

    instructor_encontrado = False

    for instructor in listaInstructores:
        if instructor["IdInstructor"] == str(idInstructor) and instructor["Activo"] == "Activo":
            instructor_encontrado = True

            if campo == 1:
                nombre = input("Ingrese el nuevo nombre: ")
                instructor["Nombre"] = nombre
                print("Nombre modificado con éxito.")

            elif campo == 2:
                apellido = input("Ingrese el nuevo apellido: ")
                instructor["Apellido"] = apellido
                print("Apellido modificado con éxito.")

            elif campo == 3:
                fechaNac = input("Ingrese la nueva fecha de nacimiento: ")
                instructor["FechaNac"] = fechaNac
                print("Fecha de nacimiento modificada con éxito.")

            elif campo == 4:
                print("Saliendo de la edición.")
            else:
                print("Campo inválido.")

            input("Presione una tecla para continuar...")


    if not instructor_encontrado:
        print("Instructor no encontrado o inactivo.")
        input("Presione una tecla para continuar...")
