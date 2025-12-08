import re
from datetime import datetime
import json


#Funcion de limpieza de interfaz, Imprime 50 bajadas de linea
def clear():
    print("\n" * 50)



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

def esClaseDisponible(archivo):
    """
    Solicita al usuario un día y una hora, y verifica que no haya
    otra clase activa en el mismo horario. Devuelve el día y la hora válidos.
    """
    try: 
        with open(archivo, 'r', encoding="UTF-8") as datos:
            clases = json.load(datos)

        
        while True:
            dia = validarOpcion("Ingrese el día de la clase: ", ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"])
            hora = validarOpcion("Ingrese la hora de la clase: ", [
                "07:00", "08:00", "09:00", "10:00", "11:00", "12:00", "13:00",
                "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00", "21:00", "22:00"
            ])

            # Validación contra clases activas
            conflicto = False
            for clase in clases:
                if clase["Activo"].lower() == "activo" and clase["Dia"].lower() == dia.lower() and clase["Hora"] == hora:
                    conflicto = True
                    print(f" Ya existe una clase activa el {dia} a las {hora}. Elegí otro horario.")


            if not conflicto:
                print(f" Horario disponible: {dia} a las {hora}")
                return dia.capitalize(), hora
    except (FileNotFoundError, OSError) as error:
        print(f"Error! {error}")

            
def validarSocio(diccionario, id):
    encontrado = list(filter(lambda s: s["IdSocio"] == id and s["Activo"] == "Activo", diccionario))

    if len(encontrado) > 0:
        return True
    else:
        return False


def validarClase(diccionario, id):
    encontrado = list(filter(lambda c: c["IdClase"] == id and c["Activo"] == "Activo", diccionario))

    if len(encontrado) > 0:
        return True
    else:
        return False

def validarInstructor(diccionario, id):
    encontrado = list(filter(lambda i: i["IdInstructor"] == id and i["Activo"] == "Activo", diccionario))

    if len(encontrado) > 0:
        return True
    else:
        return False

def validarFecha(fecha):

    patron = r'^\d{2}/\d{2}/\d{4}$'

    if not re.match(patron, fecha):
        return False
    
    try:
        datetime.strptime(fecha, "%d/%m/%Y")
        return True
    except ValueError:
        return False

def validarNombre():
    while True:
        nombre = input("Ingrese el nuevo nombre: ")
        if re.fullmatch(r"[A-Za-z]+", nombre):
            return nombre
        else:
            print("Error, el nombre solo debe contener letras.")

def validarApellido():
    while True:
        apellido = input("Ingrese el nuevo apellido: ")
        if re.fullmatch(r"[A-Za-z]+", apellido):
            return apellido
        else:
            print("Error, el apellido solo debe contener letras.")


