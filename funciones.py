
from datos import socios, clases, asistencias, instructores




def clear():
    print("\n" * 50)

#--------------------- Funciones relacionadas a la entidad Socios ------------------------


def crearSocio(socios):
    print("\n=== Crear socio ===")
    id_socio = str(len(socios)+1)  # esto genera el id del socio
    nombre = input("Ingrese el nombre: ")
    apellido = input("Ingrese el apellido: ")
    fecha = input("Ingrese la fecha de nacimiento de la siguiente forma (dd/mm/aaaa): ")
    abono = validarOpcion("Tipo de abono (Efectivo/Transferencia): ", ["Efectivo", "Transferencia"])
    estado = validarOpcion("Estado del pago (Pago/NoPago): ", ["Pago", "NoPago"])

    nuevo = {
        "IdSocio": id_socio,
        "Nombre": nombre,
        "Apellido": apellido,
        "FechaNac": fecha,
        "TipoAbono": abono,
        "EstadoPago": estado,
        "Activo": "Activo"
    }

    socios.append(nuevo)
    print("Socio agregado con éxito.")

def darBajaSocio(listaSocios, idSocio):
    for socio in listaSocios:
        if socio["IdSocio"] == str(idSocio):
            if socio["Activo"] == "Activo":
                socio["Activo"] = "Inactivo"
                return f"Socio {socio['Nombre']} {socio['Apellido']} dado de baja."
            else:
                return f"El socio {socio['Nombre']} {socio['Apellido']} ya estaba inactivo."
    print("Socio no encontrado.")

def darAltaSocio(listaSocios, idSocio):
    for socio in listaSocios:
        if socio["IdSocio"] == str(idSocio):
            if socio["Activo"] == "Inactivo":
                socio["Activo"] = "Activo"
                return f"Socio {socio['Nombre']} {socio['Apellido']} dado de alta."
            else:
                return f"El socio {socio['Nombre']} {socio['Apellido']} ya estaba activo."
    print("Socio no encontrado.")


def mostrarSocios(socios):
    clear()
    encabezados = ["IdSocio", "Nombre", "Apellido", "FechaNac", "TipoAbono", "EstadoPago", "Activo"]
    print(" | ".join([e.center(15) for e in encabezados]))
    print("-" * (len(encabezados) * 18))

    for socio in socios:
        if socio["Activo"] in ["Activo", "Inactivo"]:
            fila = [
                socio["IdSocio"],
                socio["Nombre"],
                socio["Apellido"],
                socio["FechaNac"],
                socio["TipoAbono"],
                socio["EstadoPago"],
                socio["Activo"]
            ]
            print(" | ".join([dato.center(15) for dato in fila]))

    input("Presione una tecla para continuar.")

def editarSocios(listaSocios, idSocio):
    clear()
    print("\n=== Editar Socio ===")
    print("1. Editar Nombre")
    print("2. Editar Apellido")
    print("3. Editar Tipo de Abono")
    print("4. Salir")
    campo = int(input("Ingrese el campo a modificar: "))

    socio_encontrado = False

    for socio in listaSocios:
        if socio["IdSocio"] == str(idSocio) and socio["Activo"] == "Activo":
            socio_encontrado = True

            if campo == 1:
                nombre = input("Ingrese el nuevo nombre: ")
                socio["Nombre"] = nombre
                print("Nombre modificado con éxito.")

            elif campo == 2:
                apellido = input("Ingrese el nuevo apellido: ")
                socio["Apellido"] = apellido
                print("Apellido modificado con éxito.")

            elif campo == 3:
                abono = input("Tipo de abono (Efectivo/Transferencia): ")
                socio["TipoAbono"] = abono
                print("Tipo de abono modificado con éxito.")

            elif campo == 4:
                print("Saliendo de la edición.")
            else:
                print("El campo seleccionado no existe.")

            input("Presione una tecla para continuar...")
            break  # ya encontramos y editamos al socio, salimos del bucle

    if not socio_encontrado:
        print("Socio no encontrado o inactivo.")
        input("Presione una tecla para continuar...")


#--------------------- Funciones relacionadas a la entidad Clases ------------------------

def crearClases(clases):
    print("\n=== Crear Clase ===")
    id_clase = str(len(clases) + 1)
    nombreClase = input("Ingrese el nombre de la clase: ")
    dia = validarOpcion("Ingrese el día de la clase: ", ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"])
    hora = validarOpcion("Ingrese la hora de la clase: ", [ "07:00", "08:00", "09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00", "21:00", "22:00"])
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
    print("Clase agregada con éxito.")


def darBajaClase(listaClases, idClase):
    for clase in listaClases:
        if clase["IdClase"] == str(idClase):
            if clase["Activo"] == "Activo":
                clase["Activo"] = "Inactivo"
                return f"Clase {clase['NombreClase']} dada de baja."
            else:
                return f"La clase {clase['NombreClase']} ya estaba inactiva."
    print("Clase no encontrada.")


def darAltaClase(listaClases, idClase):
    for clase in listaClases:
        if clase["IdClase"] == str(idClase):
            if clase["Activo"] == "Inactivo":
                clase["Activo"] = "Activo"
                return f"Clase {clase['NombreClase']} dada de alta."
            else:
                return f"La clase {clase['NombreClase']} ya estaba activa."
    print("Clase no encontrada.")


def mostrarClases(clases):
    clear()
    encabezados = ["IdClase", "NombreClase", "Dia", "Hora", "IdInstructor", "Activo"]
    print(" | ".join([e.center(15) for e in encabezados]))
    print("-" * (len(encabezados) * 18))

    for clase in clases:
        if clase["Activo"] in ["Activo", "Inactivo"]:
            fila = [
                clase["IdClase"],
                clase["NombreClase"],
                clase["Dia"],
                clase["Hora"],
                clase["IdInstructor"],
                clase["Activo"]
            ]
            print(" | ".join([dato.center(15) for dato in fila]))

    input("Presione una tecla para continuar...")


def editarClases(listaClases, idClase):
    clear()
    print("\n=== Editar Clase ===")
    print("1. Nombre")
    print("2. Día")
    print("3. Hora")
    print("4. Instructor")
    print("5. Salir")
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

            elif campo == 5:
                print("Saliendo de la edición.")
            else:
                print("Campo inválido.")

            input("Presione una tecla para continuar...")
            break

    if not clase_encontrada:
        print("Clase no encontrada o inactiva.")
        input("Presione una tecla para continuar...")


#--------------------- Funciones relacionadas a la entidad Instructores ------------------------

def crearInstructor(instructores):
    print("\n=== Crear Instructor ===")
    id_instructor = str(len(instructores) + 1)
    nombre = input("Ingrese el nombre: ")
    apellido = input("Ingrese el apellido: ")
    fechaNac = input("Ingrese la fecha de nacimiento: ")

    nuevo = {
        "IdInstructor": id_instructor,
        "Nombre": nombre,
        "Apellido": apellido,
        "FechaNac": fechaNac,
        "Activo": "Activo"
    }

    instructores.append(nuevo)
    print("Instructor agregado con éxito.")


def darBajaInstructor(listaInstructores, idInstructor):
    for instructor in listaInstructores:
        if instructor["IdInstructor"] == str(idInstructor):
            if instructor["Activo"] == "Activo":
                instructor["Activo"] = "Inactivo"
                return f"Instructor {instructor['Nombre']} {instructor['Apellido']} dado de baja."
            else:
                return f"El instructor {instructor['Nombre']} {instructor['Apellido']} ya estaba inactivo."
    print("Instructor no encontrado.")


def darAltaInstructor(listaInstructores, idInstructor):
    for instructor in listaInstructores:
        if instructor["IdInstructor"] == str(idInstructor):
            if instructor["Activo"] == "Inactivo":
                instructor["Activo"] = "Activo"
                return f"Instructor {instructor['Nombre']} {instructor['Apellido']} dado de alta."
            else:
                return f"El instructor {instructor['Nombre']} {instructor['Apellido']} ya estaba activo."
    print("Instructor no encontrado.")


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
            break

    if not instructor_encontrado:
        print("Instructor no encontrado o inactivo.")
        input("Presione una tecla para continuar...")


#-------------------------------- Otras Funciones --------------------------------------


# Funcion para logearse, si la contraseña es incorrecta no entrara al menu de administrador
def log_in():
    clear()
    print("\n=== Login ===")
    intentos = 3
    while intentos > 0:
        password = input("Ingrese la contraseña: ")
        if password == "admin123":
            print("Login exitoso.")
            return True
        else:
            intentos -= 1
            clear()
            print(f"Contraseña incorrecta. Le quedan ", intentos, " intentos")
    print("Ha agotado los intentos. Volviendo al menú principal.")
    return False



#Funcion Generica para validar respuestas del usuario

def validarOpcion(mensaje, opcionesValidas):
    """
    Pide al usuario una entrada y valida que esté en opcionesValidas.
    No distingue mayúsculas/minúsculas.
    """
    opcion = input(mensaje).strip().lower()
    opcionesValidasLower = [o.lower() for o in opcionesValidas]  # paso todas a minúscula

    while opcion not in opcionesValidasLower:
        opcion = input(f"Error, intente nuevamente.\n{mensaje}").strip().lower()

    # Devuelvo la opción tal como estaba en opcionesValidas (respeto mayúsculas originales)
    return opcionesValidas[opcionesValidasLower.index(opcion)]

