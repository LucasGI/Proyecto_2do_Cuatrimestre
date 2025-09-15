from funcionesValidacion import clear 

def menuPrincipal():
    clear()
    print("\n=== Sistema de gestion Gym")
    print("1. Gestion Socios")
    print("2. Gestion Instructores")
    print("3. Gestion Clases")
    print("4. Gestion Asistencias")
    print("5. Estadisticas")
    print("0. Salir")
    op = input("Seleccione una opcion: ")
    return op

def menuSocios():
    clear()
    print("\n=== Menu Gestion de Socios")
    print("1. Nuevo Socio")
    print("2. Alta/Baja Socio")
    print("3. Modificar Socio")
    print("4. Mostrar Socio")
    print("0. Salir")
    op = input("Seleccione una opcion: ")
    return op

def menuClases():
    clear()
    print("\n=== Menu Gestion de Clases")
    print("1. Nueva Clase")
    print("2. Alta/Baja Clase")
    print("3. Modificar Clase")
    print("4. Mostrar Clase")
    print("0. Salir")
    op = input("Seleccione una opcion: ")
    return op

def menuInstructores():
    clear()
    print("\n=== Menu Gestion de Instructores")
    print("1. Nuevo Instructor")
    print("2. Alta/Baja Instructores")
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


def menuAltaBaja():
    clear()
    print("\n=== Menu Edicion ===")
    print("1. Alta")
    print("2. Baja")
    print("0. Salir")
    op = input("Seleccione una opcion: ")
    return op


def menuAsistencias():
    clear()
    print("\n=== Menu Asistencias ===")
    print("1. Registrar Asistencia")
    print("2. Mostrar Asistencias")
    print("3. Editar Asistencia")
    print("4. Anular Asistencia")
    print("0. Salir")
    op = input("Seleccione una opcion: ")
    return op

def menuEstadisticas():
    clear()
    print("\n=== Menu Estadisticas ===")
    print("1. Cantidad de socios por tipo de abono")
    print("2. Cantidad de asistencias por clase")
    print("3. Promedio de socios activos e inactivos")
    print("4. Cantidad de clases por instructor")
    print("0. Salir")
    op = input("Seleccione una opcion: ")
    return op

