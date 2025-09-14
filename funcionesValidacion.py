
from datos import socios, clases, asistencias, instructores



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
