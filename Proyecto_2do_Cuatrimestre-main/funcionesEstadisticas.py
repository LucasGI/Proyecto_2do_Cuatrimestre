from funcionesValidacion import *
import json

def promedioActivosInactivos(archivoS):
    clear()
    try:
        with open(archivoS, 'r', encoding="UTF-8") as datos:
            socios = json.load(datos)

        activos = 0
        inactivos = 0

        for socio in socios:
            estado = socio.get('Activo', '').lower()
            if estado == 'activo':
                activos += 1
            else:
                inactivos += 1

        total = len(socios)

        if total == 0:
            print("No hay socios cargados.")
            return

        promedioActivos= lambda activos, total: (activos / total * 100) 
        promedioInactivos= lambda inactivos, total: (inactivos / total * 100)

        print("=== Estadísticas de Socios ===\n")
        print(f"Total de Socios: {total}")
        print(f"Socios Activos: {activos} ({promedioActivos(activos, total):.2f}%)")
        print(f"Socios Inactivos: {inactivos} ({promedioInactivos(inactivos, total):.2f}%)")

        input("\nPresione Enter para continuar...")
    
    except (FileNotFoundError, OSError) as error:
        print(f'Error! {error}')
        input("Presione una tecla para continuar.")
    

def cantidadSociosPorAbono(archivoS):
    clear()
    try:
        with open(archivoS, 'r', encoding="UTF-8") as datos:
            socios = json.load(datos)

        efectivo = 0
        transferencia = 0

        for socio in socios:
            abono = socio.get('TipoAbono', '').lower()
            if abono == 'efectivo':
                efectivo += 1
            elif abono == 'transferencia':
                transferencia += 1

        print("=== Cantidad de Socios por Tipo de Abono ===\n")
        print(f"Socios con abono en Efectivo: {efectivo}")
        print(f"Socios con abono por Transferencia: {transferencia}")
        print(f"Total de socios: {len(socios)}")

        input("\nPresione Enter para continuar...")

    except (FileNotFoundError, OSError) as error:
        print(f'Error! {error}')
        input("Presione una tecla para continuar.")
    


def cantidadClasesInstructor(archivoC, archivoI):
    try:
        with open(archivoC, 'r', encoding="UTF-8") as datosC:
            clases = json.load(datosC)

        with open(archivoI, 'r', encoding="UTF-8") as datosI:
            instructores = json.load(datosI)

        print("=== Cantidad de clases por instructor ===\n")

        for instructor in instructores:
            id_instructor = instructor["IdInstructor"]
            nombre_instructor = f"{instructor['Nombre']} {instructor['Apellido']}"
            contador = 0

            for clase in clases:
                if int(clase["IdInstructor"]) == id_instructor:
                    contador += 1

            print(f"Instructor: {nombre_instructor} - Total de clases: {contador}")

        input("\nPresione Enter para continuar...")
    
    except (FileNotFoundError, OSError) as error:
        print(f'Error! {error}')
        input("Presione una tecla para continuar.")

def cantidadAsistenciaPorClase(archivoC, archivoA):
    try:
        with open(archivoC, 'r', encoding="UTF-8") as datosC:
            clases = json.load(datosC)

        print("=== Cantidad de asistencias por clase ===\n")

        for clase in clases:
            id_clase = clase["IdClase"]
            nombre_clase = clase["NombreClase"]
            contador = 0

            with open(archivoA, 'r', encoding="UTF-8") as archivo:
                linea = archivo.readline()

                while linea != "":
                    partes = linea.strip().split()

                    if len(partes) >= 4:
                        id_clase_archivo = int(partes[1]) 
                        if id_clase_archivo == id_clase:
                            contador += 1

                    linea = archivo.readline()

            print(f"Clase: {nombre_clase} - Total de asistencias: {contador}")

        input("\nPresione Enter para continuar...")
    
    except (FileNotFoundError, OSError) as error:
        print(f'Error! {error}')
        input("Presione una tecla para continuar.")
