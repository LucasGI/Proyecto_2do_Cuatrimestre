from funciones import clear 

def menuPrincipal():
    clear()
    print("\n=== Sistema de gestion Gym")
    print("1. Gestion Socios")
    print("2. Gestion Instructores")
    print("3. Gestion Clases")

    print("0. Salir")
    op = input("Seleccione una opcion: ")
    return op

def menuSocios():
    clear()
    print("\n=== Menu Gestion de Socios")
    print("1. Alta Socio")
    print("2. Baja Socio")
    print("3. Modificar Socio")
    print("4. Mostrar Socio")
    print("0. Salir")
    op = input("Seleccione una opcion: ")
    return op

def menuClases():
    clear()
    print("\n=== Menu Gestion de Clases")
    print("1. Alta Clase")
    print("2. Baja Clase")
    print("3. Modificar Clase")
    print("4. Mostrar Clase")
    print("0. Salir")
    op = input("Seleccione una opcion: ")
    return op

def menuInstructores():
    clear()
    print("\n=== Menu Gestion de Instructores")
    print("1. Alta Instructores")
    print("2. Baja Instructores")
    print("3. Modificar Instructores")
    print("4. Mostrar Instructores")
    print("0. Salir")
    op = input("Seleccione una opcion: ")
    return op


def menuEdicionSocios():
    clear()
    print("\n=== Menu Edicion ===")
    print("1. Nombre")
    print("2. Apellido")
    print("3. Tipo de abono")
    print("4. Estado del pago")
    print("0. Salir")
    op = input("Seleccione una opcion: ")
    return op
