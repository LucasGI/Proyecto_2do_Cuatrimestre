from funcionesValidacion import clear, validarOpcion, validarSocio, validarFecha, validarApellido, validarNombre
import json
import re

#--------------------- Funciones relacionadas a la entidad Socios ------------------------

"""
Crear socio recibe por parametro la lista de diccionarios 'socios', luego crea en la funcion un diccionario nuevo para luego 
hacer un append en la lista de diccionarios 'socios'
"""
def crearSocio(archivo):
    
    try:
        print("\n=== Crear socio ===")
        with open(archivo, 'r', encoding="UTF-8") as datos:
            socios = json.load(datos)

        id_socio = len(socios) + 1
        nombre = validarNombre()
        apellido=validarApellido()
        gmail= nombre[0:1].upper() + apellido.lower() + "@gmail.com"
        while True:
            fechaNac = input("Ingrese la fecha de la siguiente forma (dd/mm/aaaa): ")
            if validarFecha(fechaNac):
                print("Fecha válida.")
                break
            else:
                print("FORMATO INVALIDO o fecha inválida. Use dd/mm/aaaa")
        abono = validarOpcion("Tipo de abono (Efectivo/Transferencia): ", ["Efectivo", "Transferencia"])
        estado = validarOpcion("Estado del pago (Pago/NoPago): ", ["Pago", "NoPago"])

        nuevo = {
            "IdSocio": id_socio,
            "Nombre": nombre,
            "Apellido": apellido,
            "Gmail": gmail,
            "FechaNac": fechaNac,
            "TipoAbono": abono,
            "EstadoPago": estado,
            "Activo": "Activo"
        }

        socios.append(nuevo)
        with open(archivo, 'w', encoding="UTF-8") as datos:
            json.dump(socios, datos, ensure_ascii=False)
    
    except (FileNotFoundError, OSError) as error:
        print(f'Error! {error}')
        input('Presione una tecla para continuar...')


def darBajaSocio(archivo, idSocio):
    """
    darBajaSocio recibe por parametros la lista de diccionarios 'socios' y el id del socio a dar de baja (pedido previamente en el main) y cambia 
    el campo [Activo] a "Inactivo"
    """
    try:
        with open(archivo, 'r', encoding="UTF-8") as datos:
            socios = json.load(datos)

        
        socio_validado = validarSocio(socios, idSocio)
        if not socio_validado:
            print(f"El socio con ID {idSocio} ya está inactivo.")
        else:
            encontrado = False
            for socio in socios:
                if socio["IdSocio"] == idSocio:
                    socio["Activo"] = re.sub("Activo", "Inactivo", socio["Activo"])
                    print(f"socio {socio['Nombre']} dado de baja.")
                    encontrado = True
                    break

            if not encontrado:
                print(f"No se encontró ningun socio con el ID {idSocio}.")

        with open(archivo, 'w', encoding="UTF-8") as datos:
            json.dump(socios, datos, ensure_ascii=False, indent=4)

        input('Presione una tecla para continuar...')

    except (FileNotFoundError, OSError) as error:
        print(f'Error! {error}')
        input('Presione una tecla para continuar...')


def darAltaSocio(archivo, idSocio):
    """ darAltaSocio recibe por parametros la lista de diccionarios 'socios' y el id del socio a dar de baja (pedido previamente en el main) y cambia 
    el campo [Activo] a "Activo"
    """
    try:
        with open(archivo, 'r', encoding="UTF-8") as datos:
            socios = json.load(datos)

        
        socio_validado = validarSocio(socios, idSocio)
        if socio_validado:
            print(f"El socio con ID {idSocio} ya está activo.")
        else:
            encontrado = False
            for socio in socios:
                if socio["IdSocio"] == idSocio:
                    socio["Activo"] = re.sub("Inactivo", "Activo", socio["Activo"])
                    print(f"socio {socio['Nombre']} dado de alta.")
                    encontrado = True
                    break  

            if not encontrado:
                print(f"No se encontró ningun socio con el ID {idSocio}.")

        with open(archivo, 'w', encoding="UTF-8") as datos:
            json.dump(socios, datos, ensure_ascii=False, indent=4)

        input('Presione una tecla para continuar...')

    except (FileNotFoundError, OSError) as error:
        print(f'Error! {error}')
        input('Presione una tecla para continuar...')



def mostrarSocios(archivo):
    """
    mostrarSocios recibe por parametro la lista de diccionarios 'socios' y printea por orden de legajo la lista completa de socios, solo los activos
    """
    clear()
    try:
        with open(archivo, 'r', encoding="UTF-8") as datos:
            socios = json.load(datos)
            
            socios_activos = [s for s in socios if s["Activo"] == "Activo"]
            socios_mayuscula= list(map(lambda i: {**i, "Nombre": i["Nombre"].capitalize(), "Apellido": i["Apellido"].capitalize()}, socios_activos))
            encabezados = ["IdSocio", "Nombre", "Apellido", "FechaNac", "TipoAbono", "EstadoPago", "Activo", "Gmail"]
            print(" | ".join([e.center(15) for e in encabezados]))
            print("-" * (len(encabezados) * 19))

            list(map(lambda socio: print(" | ".join([
            str(socio["IdSocio"]).center(15),
            socio["Nombre"].center(15),
            socio["Apellido"].center(15),
            socio["FechaNac"].center(15),
            socio["TipoAbono"].center(15),
            socio["EstadoPago"].center(15),
            socio["Activo"].center(15),
            socio["Gmail"].center(15)
        ])), socios_mayuscula))

        print(f"Total de instructores activos: {len(socios_mayuscula)}")
        input("Presione una tecla para continuar...")
        
    except (FileNotFoundError, OSError) as error:
        print(f'Error! {error}')
        input("Presione una tecla para continuar.")


def editarSocios(archivo, idSocio):
    """
    editarSocios recibe por parametro la lista de diccionarios 'socios' y el id del socio a modificar. luego pregunta que campo del diccionario
    se quiere editar. solo se pueden editar socios en estado 'Activo'
    """
    try:
        with open(archivo, 'r', encoding="UTF-8") as datos:
            socios = json.load(datos)
        
        if not validarSocio(socios, idSocio):
            print('Socio no encontrado o inactivo')
            input("presione una tecla para continuar...")
            return

        for socio in socios:
            if socio["IdSocio"] == idSocio:
                clear()
                print("\n=== Editar Socio ===")
                print("1. Editar Nombre")
                print("2. Editar Apellido")
                print("4. Editar Fecha de nacimiento")
                print("3. Editar Tipo de Abono")
                print("0. Salir")
                campo = int(input("Ingrese el campo a modificar: "))
                
                if campo == 1:
                    nombre = validarNombre()
                    socio["Nombre"] = nombre
                    print("Nombre modificado con éxito.")

                elif campo == 2:
                    apellido = validarApellido()
                    socio["Apellido"] = apellido
                    print("Apellido modificado con éxito.")

                elif campo == 3:
                    abono = input("Tipo de abono (Efectivo/Transferencia): ")
                    socio["TipoAbono"] = abono
                    print("Tipo de abono modificado con éxito.")

                elif campo==4:
                    fechaNac=validarFecha()
                    socio["FechaNac"] = fechaNac
                    print("Fecha de nacimiento modificada con exito")

                elif campo == 0:
                    print("Saliendo de la edición.")
                else:
                    print("El campo seleccionado no existe.")

                with open(archivo, 'w', encoding="UTF-8") as datos:
                    json.dump(socios, datos, ensure_ascii=False)

                input("Presione una tecla para continuar...")
                break
    
    except (FileNotFoundError, OSError) as error:
        print(f'Error {error}')
        input('Presione una tecla para continuar...')


mostrarSocios("archivos/socios.json")