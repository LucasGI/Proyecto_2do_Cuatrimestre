from datos import socios, clases, asistencias, instructores
from funciones import clear, validarOpcion

#--------------------- Funciones relacionadas a la entidad Socios ------------------------

"""
Crear socio recibe por parametro la lista de diccionarios 'socios', luego crea en la funcion un diccionario nuevo para luego 
hacer un append en la lista de diccionarios 'socios'
"""
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

"""
darBajaSocio recibe por parametros la lista de diccionarios 'socios' y el id del socio a dar de baja (pedido previamente en el main) y cambia 
el campo [Activo] a "Inactivo"
"""
def darBajaSocio(listaSocios, idSocio):
    for socio in listaSocios:
        if socio["IdSocio"] == str(idSocio):
            if socio["Activo"] == "Activo":
                socio["Activo"] = "Inactivo"
                return f"Socio {socio['Nombre']} {socio['Apellido']} dado de baja."
            else:
                return f"El socio {socio['Nombre']} {socio['Apellido']} ya estaba inactivo."
    print("Socio no encontrado.")

""" darAltaSocio recibe por parametros la lista de diccionarios 'socios' y el id del socio a dar de baja (pedido previamente en el main) y cambia 
el campo [Activo] a "Activo"
"""
def darAltaSocio(listaSocios, idSocio):
    for socio in listaSocios:
        if socio["IdSocio"] == str(idSocio):
            if socio["Activo"] == "Inactivo":
                socio["Activo"] = "Activo"
                return f"Socio {socio['Nombre']} {socio['Apellido']} dado de alta."
            else:
                return f"El socio {socio['Nombre']} {socio['Apellido']} ya estaba activo."
    print("Socio no encontrado.")


"""
mostrarSocios recibe por parametro la lista de diccionarios 'socios' y printea por orden de legajo la lista completa de socios, tanto
inactivos como activos
"""
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

"""
editarSocios recibe por parametro la lista de diccionarios 'socios' y el id del socio a modificar. luego pregunta que campo del diccionario
se quiere editar. solo se pueden editar socios en estado 'Activo'
"""
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

    if not socio_encontrado:
        print("Socio no encontrado o inactivo.")
        input("Presione una tecla para continuar...")