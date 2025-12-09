from funcionesValidacion import *
import json

def porcentajeActivosInactivos(archivoS):
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
        
        porcentajeActivos= lambda activos, total: (activos / total * 100) 
        porcentajeInactivos= lambda inactivos, total: (inactivos / total * 100)
        print("============================ Estadísticas de Socios ============================= \n")
        encabezados = ["Total socios", "Socios Activos", "Socios Inactivos"]
        print(" | " .join([e.center(25) for e in encabezados]))
        print("-" * len(encabezados) * 27)
        fila = [
            str(total),
            f"{activos} ({porcentajeActivos(activos, total)}%)",
            f"{inactivos} ({porcentajeInactivos(inactivos, total)}%)"
        ]
        print(" | ".join([dato.center(25) for dato in fila]))

        input("\nPresione Enter para continuar...")
    
    except (FileNotFoundError, OSError) as error:
        print(f'Error! {error}')
        input("Presione una tecla para continuar.")


def cantidadSociosPorAbonoRecursivo(archivoS, socios=None, indice=0, efectivo=0, transferencia=0):
    try:
      
        if socios is None:
            with open(archivoS, 'r', encoding="UTF-8") as datos:
                socios = json.load(datos)
            print("============== Cantidad de Socios por Tipo de Abono ==============\n")
            encabezados = ["Socios con abono en efectivo", "Socios con abono en transferencia"]
            print(" | " .join([e.center(25) for e in encabezados]))
            print("-" * len(encabezados) * 33)



        if indice >= len(socios):
            fila = [
                str(efectivo),
                str(transferencia)
            ]
            print(" | ".join([dato.center(28) for dato in fila]))
            input("\nPresione Enter para continuar...")
            return

       
        socio = socios[indice]
        abono = socio.get('TipoAbono', '').lower()

        if abono == 'efectivo':
            efectivo += 1
        elif abono == 'transferencia':
            transferencia += 1

       
        cantidadSociosPorAbonoRecursivo(archivoS, socios, indice + 1, efectivo, transferencia)

    except (FileNotFoundError, OSError) as error:
        print(f"Error! {error}")
        input("Presione una tecla para continuar.")
    


def cantidadClasesInstructor(archivoC, archivoI):
    try:
        with open(archivoC, 'r', encoding="UTF-8") as datosC:
            clases = json.load(datosC)

        with open(archivoI, 'r', encoding="UTF-8") as datosI:
            instructores = json.load(datosI)

        print("========= Cantidad de clases por instructor ==========\n")
        encabezados = ["Instructor", "Total de clases"]
        print(" | " .join([e.center(25) for e in encabezados]))
        print('-' * len(encabezados) * 27)


        for instructor in instructores:
            id_instructor = instructor["IdInstructor"]
            nombre_instructor = f"{instructor['Nombre']} {instructor['Apellido']}"
            contador = 0

            for clase in clases:
                if int(clase["IdInstructor"]) == id_instructor:
                    contador += 1

            fila = [
                str(nombre_instructor),
                str(contador)
            ]
            print(" | ".join([dato.center(25) for dato in fila]))

        input("\nPresione Enter para continuar...")
    
    except (FileNotFoundError, OSError) as error:
        print(f'Error! {error}')
        input("Presione una tecla para continuar.")


def cantidadAsistenciaPorClase(archivoC, archivoA):
    try:
        with open(archivoC, 'r', encoding="UTF-8") as datosC:
            clases = json.load(datosC)

        print("======================= Cantidad de asistencias por clase ======================\n")
        encabezados = ["Clase", "Total de asistencias"]
        print(" | " .join([e.center(40) for e in encabezados]))
        print('-' * len(encabezados) * 40)

        for clase in clases:
            id_clase = clase["IdClase"]
            nombre_clase = f"{clase['NombreClase']}  ({clase['Dia']} {clase['Hora']})"
            contador = 0

            with open(archivoA, 'r', encoding="UTF-8") as archivo:

                for linea in archivo:
                    partes = linea.strip().split()

                    if len(partes) >= 4:
                        id_clase_archivo = int(partes[1]) 
                        if id_clase_archivo == id_clase:
                            contador += 1

            fila = [
                nombre_clase,
                str(contador)
            ]
            print(" | ".join([dato.center(40) for dato in fila]))

        input("\nPresione Enter para continuar...")
    
    except (FileNotFoundError, OSError) as error:
        print(f'Error! {error}')
        input("Presione una tecla para continuar.")







def cantidadAsistenciasPorSocioRecursivo(archivoS, archivoA, indice=0, socios=None, asistencias=None):
    """
    Calcula recursivamente la cantidad de asistencias por cada socio.
    """
    try:
        
        if socios is None:
            with open(archivoS, 'r', encoding="UTF-8") as datosS:
                socios = json.load(datosS)

            asistencias = []
            with open(archivoA, 'r', encoding="UTF-8") as datosA:
                for linea in datosA:
                    asistencias.append(linea)

            print("========= Cantidad de asistencias por socio  ========= \n")
            encabezados = ["Socio", "Total Asistencias"]
            print(" | " .join([e.center(25) for e in encabezados]))
            print("-" * len(encabezados) * 27)

        
        if indice >= len(socios):
            input("Presione Enter para continuar...")
            return

        socio = socios[indice]
        id_socio = socio["IdSocio"]
        nombre_socio = f'{socio["Nombre"]} {socio["Apellido"]}'
        
        
        contador = sum(1 for linea in asistencias 
        if len(linea.strip().split()) >= 4 and int(linea.strip().split()[3]) == id_socio)
        
        
        fila = [
            str(nombre_socio),
            str(contador)
        ]
        print(" | ".join([dato.center(25) for dato in fila]))
        
        cantidadAsistenciasPorSocioRecursivo(archivoS, archivoA, indice + 1, socios, asistencias)

    except (FileNotFoundError, OSError) as error:
        print(f'Error! {error}')
        input("Presione una tecla para continuar.")
