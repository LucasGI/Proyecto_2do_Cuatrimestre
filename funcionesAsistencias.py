from datos import socios, clases, instructores
from funcionesValidacion import clear, validarOpcion, validarClase, validarSocio
import json
#--------------------- Funciones relacionadas a la entidad Asistencias ------------------------



def buscarSociosEnClase(archivoC, archivoS, archivoA, id_socio):
    clear()
    try:
        with open(archivoC, 'r', encoding="UTF-8") as datos:
            clases = json.load(datos)

        with open(archivoS, 'r', encoding="UTF-8") as datos:
            socios = json.load(datos)

        socio_encontrado = validarSocio(socios, id_socio)
        if socio_encontrado:
            for socio in socios:
                if socio["IdSocio"] == id_socio:
                        socio_encontrado = socio
                        break

        if not socio_encontrado:
            print("Socio no encontrado o inactivo.")
            return

        print(f"\n=== Asistencias del socio {socio_encontrado['Nombre']} {socio_encontrado['Apellido']} ===\n")

        with open(archivoA, 'r', encoding="UTF-8") as datos:
            lineas = datos.readline()
            
            asistencias_encontradas = False

            while lineas != "":
                partes = lineas.strip().split()
                if len(partes) >= 4:
                    id_clase = int(partes[1])
                    fecha = partes[2]
                    id_socio_archivo = int(partes[3])

                    if id_socio_archivo == id_socio:
                        for c in clases:
                            if c["IdClase"] == id_clase:
                                print(f"- Clase: {c['NombreClase']} | Día: {c['Dia']} | Fecha asistencia: {fecha}")
                                asistencias_encontradas = True
                                break
                lineas = datos.readline()

            if not asistencias_encontradas:
                print("El socio no tiene asistencias registradas.")    
    

    except (FileNotFoundError, OSError) as error:
        print(f'Error! {error}')
        input("Presione una tecla para continuar.")



def buscarClaseYAsistencias(archivoC, archivoS, archivoA, id_clase):
    clear()
    try:
        with open(archivoC, 'r', encoding="UTF-8") as datosC:
            clases = json.load(datosC)

        with open(archivoS, 'r', encoding="UTF-8") as datosS:
            socios = json.load(datosS)

        clase_encontrada = validarClase(socios, id_socio)
        if clase_encontrada:
            for clase in clases:
                if clase["IdSocio"] == id_clase:
                        clase_encontrada = clase
                        break

        if not clase_encontrada:
            print("No se encontró la clase con ese ID.")
            return

        print(f"\n=== Socios que asistieron a la clase '{clase_encontrada['NombreClase']}' ({clase_encontrada['Dia']} {clase_encontrada['Hora']}) ===\n")

        with open(archivoA, 'r', encoding="UTF-8") as datosA:
            linea = datosA.readline()
            asistencias_encontradas = False

            while linea != "":
                partes = linea.strip().split()
                if len(partes) >= 4:
                    id_clase_archivo = int(partes[1])
                    fecha = partes[2]
                    id_socio = int(partes[3])

                    if id_clase_archivo == id_clase:
                        for socio in socios:
                            if socio["IdSocio"] == id_socio:
                                print(f"- {socio['Nombre']} {socio['Apellido']} | Fecha: {fecha}")
                                asistencias_encontradas = True
                                break

                linea = datosA.readline()

        if not asistencias_encontradas:
            print("No hay socios registrados en esta clase.")

    except FileNotFoundError:
        print("Alguno de los archivos no se encontró.")
    except json.JSONDecodeError:
        print("Error al leer los archivos JSON.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

buscarClaseYAsistencias("archivos/clases.json","archivos/socios.json","asistencias.txt", 2)
"""
def crearAsistencias(asistencia):
    print("\n=== Crear asistencia ===")
    id_asistencia = str(len(asistencia) + 1)
    id_socio = input("Ingrese el id del socio: ")
    id_clase = input("Ingrese el ID de la clase: ")
    id
    fecha = input("Ingrese la fecha de la clase: ")

    nuevo = {
        "IdAsistencia": id_asistencia,
        "IdSocio": id_socio,
        "IdClase": id_clase,

        "Fecha": fecha

    }

    asistencias.append(nuevo)
    print("Clase agregada con éxito.")



def registrarAsistencia(asistencias, socios, clases):
    print("\n=== Registrar Asistencia ===")
    id_asistencia = str(len(asistencias) + 1)
    id_socio = input("Ingrese el ID del socio: ")
    id_clase = input("Ingrese el ID de la clase: ")
    
    # Validar que el socio y la clase existan
    socio_valido = validarSocio(socios, id_socio)
    clase_valida = validarClase(clases, id_clase)

    if not socio_valido:
        return "Socio no encontrado o inactivo."
    if not clase_valida:
        return "Clase no encontrada o inactiva."

    nuevo = {
        "IdAsistencia": id_asistencia,
        "IdSocio": id_socio,
        "IdClase": id_clase
    }

    asistencias.append(nuevo)
    print("Asistencia registrada con éxito.")
    input("Presione Enter para continuar...")

def anularAsistencia(asistencias, idAsistencia):
    asistencia_encontrada = False
    for asistencia in asistencias:
        if asistencia["IdAsistencia"] == str(idAsistencia):
            asistencias.remove(asistencia)
            print (f"Asistencia {idAsistencia} anulada.")
            input("Presione Enter para continuar...")
            asistencia_encontrada = True
    if not asistencia_encontrada:
        print("Asistencia no encontrada.")
        input("Presione Enter para continuar...")
    

def mostrarAsistencias(asistencias, socios, clases):
    clear()
    encabezados = ["IdAsistencia", "Nombre Socio", "Nombre Clase"]
    print(" | ".join(encabezados))
    print("-" * 55)
    for asistencia in asistencias:
        # Buscar el socio por IdSocio
        nombre_socio = "Desconocido"
        for s in socios:
            if s["IdSocio"] == asistencia["IdSocio"]:
                nombre_socio = f'{s["Nombre"]} {s["Apellido"]}'
                
        # Buscar la clase por IdClase
        nombre_clase = "Desconocido"
        for c in clases:
            if c["IdClase"] == asistencia["IdClase"]:
                nombre_clase = c["NombreClase"]
                
                print(" | ".join([
            str(asistencia["IdAsistencia"]).ljust(15),
            nombre_socio.ljust(20),
            nombre_clase.ljust(20)
        ]))
    input("\nPresione Enter para continuar...")

def editarAsistencia(asistencias, idAsistencia):
    for asistencia in asistencias:
        if asistencia["IdAsistencia"] == str(idAsistencia):
            print(f"\n=== Editar Asistencia {idAsistencia} ===")
            nuevo_id_socio = input(f"Nuevo ID del socio (actual: {asistencia['IdSocio']}): ")
            nuevo_id_clase = input(f"Nuevo ID de la clase (actual: {asistencia['IdClase']}): ")

            if nuevo_id_socio:
                asistencia["IdSocio"] = nuevo_id_socio
            if nuevo_id_clase:
                asistencia["IdClase"] = nuevo_id_clase

            print("Asistencia actualizada con éxito.")
            input("Presione Enter para continuar...")
            return
    print("Asistencia no encontrada.")
    input("Presione Enter para continuar...")
"""
"""""
def mostrarAsistencias(archivoA, socios, clases):
    clear()
    
    encabezados = ["IdAsistencia", "Nombre Socio", "Nombre Clase"]
    print(" | ".join(encabezados))
    print("-" * 55)

    try:
        with open(archivoA, 'r', encoding="UTF-8") as datosA:
            linea = datosA.readline()

        ultAsistencias = []

    try:
        with open(archivoA, 'r', encoding="UTF-8") as datos:
            instructores = json.load(datos)
        
        encabezados = ["IdInstructor", "Nombre", "Apellido", "FechaNac", "Activo"]
        print(" | ".join([e.center(15) for e in encabezados]))
        print("-" * (len(encabezados) * 18))

        for instructor in instructores:
            if instructor["Activo"] in ["Activo"]:
                fila = [
                    str(instructor["IdInstructor"]),
                    instructor["Nombre"],
                    instructor["Apellido"],
    
    with open(archivoA, 'r', encoding="UTF-8") as datos: """""""""
        
"""  ultimas_asistencias = asistencias[-5:]

    for asistencia in asistencias:
        # Buscar el socio por IdSocio
        nombre_socio = "Desconocido"
        for s in socios:
            if s["IdSocio"] == asistencia["IdSocio"]:
                nombre_socio = f'{s["Nombre"]} {s["Apellido"]}'
                
        # Buscar la clase por IdClase
        nombre_clase = "Desconocido"
        for c in clases:
            if c["IdClase"] == asistencia["IdClase"]:
                nombre_clase = c["NombreClase"]
                
                print(" | ".join([
            str(asistencia["IdAsistencia"]).ljust(15),
            nombre_socio.ljust(20),
            nombre_clase.ljust(20)
        ])) """
 #   input("\nPresione Enter para continuar...")

    
