from funcionesValidacion import *
import json
#--------------------- Funciones relacionadas a la entidad Asistencias ------------------------



def mostrarClasesPorSocio(archivoC, archivoS, archivoA, id_socio):
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
                if len(partes) == 4:
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

        input("Presione Enter para continuar...")
    

    except (FileNotFoundError, OSError) as error:
        print(f'Error! {error}')
        input("Presione una tecla para continuar.")



def mostrarSociosPorClase(archivoC, archivoS, archivoA, id_clase):
    clear()
    try:
        with open(archivoC, 'r', encoding="UTF-8") as datosC:
            clases = json.load(datosC)

        with open(archivoS, 'r', encoding="UTF-8") as datosS:
            socios = json.load(datosS)

        clase_encontrada = validarClase(clases, id_clase)
        if clase_encontrada:
            for clase in clases:
                if clase["IdClase"] == id_clase:
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
                if len(partes) == 4:
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
        
        input("Presione Enter para continuar...")

    except (FileNotFoundError, OSError) as e:
        print(f"Ocurrió un error: {e}")
        input("Presione una tecla para continuar.")




def mostrarAsistenciasPorInstructor(archivoC, archivoS, archivoI, archivoA, id_instructor):
    clear()
    try:
        with open(archivoC, 'r', encoding="UTF-8") as datosC:
            clases = json.load(datosC)

        with open(archivoS, 'r', encoding="UTF-8") as datosS:
            socios = json.load(datosS)

        with open(archivoI, 'r', encoding="UTF-8") as datosI:
            instructores = json.load(datosI)

        instructor_encontrado = validarInstructor(instructores, id_instructor)
        if instructor_encontrado:
            for instructor in instructores:
                if instructor["IdInstructor"] == id_instructor:
                        instructor_encontrado = instructor
                        break

        if not instructor_encontrado:
            print("No se encontró el instructor con ese ID.")
            return

        print(f"\n=== Asistencias de las clases dictadas por {instructor_encontrado['Nombre']} {instructor_encontrado['Apellido']} ===\n")

        clases_instructor = []
        for clase in clases:
            if int(clase["IdInstructor"]) == id_instructor:
                clases_instructor.append(clase)

        if len(clases_instructor) == 0:
            print("Este instructor no dicta ninguna clase.")
            return

        with open(archivoA, 'r', encoding="UTF-8") as datosA:
            linea = datosA.readline()
            asistencias_encontradas = False

            while linea != "":
                partes = linea.strip().split()
                if len(partes) == 4:
                    id_clase = int(partes[1])
                    fecha = partes[2]
                    id_socio = int(partes[3])

                    for clase in clases_instructor:
                        if clase["IdClase"] == id_clase:
                            for s in socios:
                                if s["IdSocio"] == id_socio:
                                    print(f"Clase: {clase['NombreClase']} ({clase['Dia']} {clase['Hora']}) | Socio: {s['Nombre']} {s['Apellido']} | Fecha: {fecha}")
                                    asistencias_encontradas = True
                                    break

                linea = datosA.readline()

        if not asistencias_encontradas:
            print("No hay asistencias registradas para este instructor.")
        
        input("Presione Enter para continuar...")

    except (FileNotFoundError, OSError) as e:
        print(f"Ocurrió un error: {e}")
        input("Presione una tecla para continuar.")







def registrarAsistencia(archivoC, archivoS, archivoA):
    clear()
    try:
        with open(archivoC, 'r', encoding="UTF-8") as datosC:
            clases = json.load(datosC)
        with open(archivoS, 'r', encoding="UTF-8") as datosS:
            socios = json.load(datosS)

        id_socio = int(input("Ingrese el ID de el socio que asistio"))
        socio_encontrado = validarSocio(socios, id_socio)
        if socio_encontrado:
            for socio in socios:
                if socio["IdSocio"] == id_socio:
                        socio_encontrado = socio
                        break
        if not socio_encontrado:
            print("Socio no encontrado o inactivo.")
            input("Presione Enter para continuar...")
            return

        print(f"\n=== Registrar Asistencia para {socio_encontrado['Nombre']} {socio_encontrado['Apellido']} ===\n")
        print("Clases disponibles:")
        for clase in clases:
            print(f"- ID: {clase['IdClase']} | Nombre: {clase['NombreClase']} | Día: {clase['Dia']} | Hora: {clase['Hora']}")

        id_clase = int(input("\nIngrese el ID de la clase a la que asistió: "))
        clase_valida = validarClase(clases, id_clase)
        if not clase_valida:
            print("Clase no encontrada.")
            input("Presione Enter para continuar...")
            return

        fecha_asistencia=validarFecha()
    
        nueva_id_asistencia = 1
        try:
            with open(archivoA, 'r', encoding="UTF-8") as archivo:
                ultima_linea = ""
                linea = archivo.readline()
                while linea:
                    ultima_linea = linea.strip()
                    linea = archivo.readline()
                if ultima_linea:
                    partes = ultima_linea.split()
                    nueva_id_asistencia = int(partes[0]) + 1
        except FileNotFoundError:
            nueva_id_asistencia = 1


        with open(archivoA, 'a', encoding="UTF-8") as datosA:
            datosA.write(f"{nueva_id_asistencia}   {id_clase}   {fecha_asistencia}   {id_socio}\n")
        input("Asistencia registrada con éxito. Presione Enter para continuar...")

    except (FileNotFoundError, OSError) as e:
        print(f"Ocurrió un error: {e}")
        input("Presione una tecla para continuar.")
    



def anularAsistencia(archivoA):
    clear()
    try:
        print("=== Lista de asistencias registradas ===\n")
        with open(archivoA, 'r', encoding="UTF-8") as archivo:
            existe = False
            linea = archivo.readline()
            while linea:
                if linea.strip():
                    print(linea.strip())
                    existe = True
                linea = archivo.readline()
            
        if not existe:
            print("No hay asistencias registradas.")
            input("Presione Enter para continuar...")
            return

       
        id_anular = input("\nIngrese el ID de la asistencia a anular: ")

        
        with open(archivoA, 'r', encoding="UTF-8") as archivo:
            lineas_restantes = []
            linea = archivo.readline()
            while linea:
                partes = linea.strip().split()
                if partes and partes[0] != id_anular:
                    lineas_restantes.append(linea)
                linea = archivo.readline()

        
        with open(archivoA, 'w', encoding="UTF-8") as archivo:
            for l in lineas_restantes:
                archivo.write(l)

        print(f"Asistencia con ID {id_anular} anulada correctamente.")
        input("Presione Enter para continuar...")

    except FileNotFoundError:
        print("El archivo de asistencias no existe.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")




def editarAsistencia(archivo, idAsistencia):
    clear()
    try:
        with open(archivo, 'r', encoding="UTF-8") as datos:
            lineas = []
            linea = datos.readline()
            encontrado = False

            while linea:
                partes = linea.strip().split()
                if len(partes) == 4 and partes[0] == str(idAsistencia):
                    encontrado = True
                    print(f"\n=== Editar Asistencia {idAsistencia} ===")
                    print(f"ID Clase actual: {partes[1]}")
                    print(f"Fecha actual: {partes[2]}")
                    print(f"ID Socio actual: {partes[3]}")

                    nuevo_id_clase = input("Nuevo ID de la clase (dejar vacío para mantener): ")
                    nueva_fecha = input("Nueva fecha (dejar vacío para mantener): ")
                    nuevo_id_socio = input("Nuevo ID del socio (dejar vacío para mantener): ")

                    if nuevo_id_clase == "":
                        nuevo_id_clase = partes[1]
                    if nueva_fecha == "":
                        nueva_fecha = partes[2]
                    if nuevo_id_socio == "":
                        nuevo_id_socio = partes[3]

                    nueva_linea = f"{partes[0]} {nuevo_id_clase} {nueva_fecha} {nuevo_id_socio}\n"
                    lineas.append(nueva_linea)
                    print("\nAsistencia actualizada con éxito.")
                else:
                    lineas.append(linea)
                
                linea = datos.readline()

        if not encontrado:
            print("\nNo se encontró una asistencia con ese ID.")

        with open(archivo, 'w', encoding="UTF-8") as datos:
            datos.writelines(lineas)

        input("\nPresione Enter para continuar...")

    except (FileNotFoundError, OSError) as error:
        print(f"Error! {error}")
        input("Presione una tecla para continuar...")
    


def mostrarAsistencias(archivoA, archivoC, archivoS):
    """
    Muestra todas las asistencias registradas en formato de tabla,
    reemplazando los IDs por los nombres correspondientes de clase y socio.
    """
    clear()
    try:
        with open(archivoC, 'r', encoding="UTF-8") as datosC:
            clases = json.load(datosC)
        with open(archivoS, 'r', encoding="UTF-8") as datosS:
            socios = json.load(datosS)

        encabezados = ["IdAsistencia", "Clase", "Fecha", "Socio"]
        print(" | ".join([e.center(20) for e in encabezados]))
        print("-" * (len(encabezados) * 23))

        with open(archivoA, 'r', encoding="UTF-8") as archivoA:
            linea = archivoA.readline()
            hay_asistencias = False

            while linea != "":
                partes = linea.strip().split()
                if len(partes) == 4:
                    id_asistencia = partes[0]
                    id_clase = int(partes[1])
                    fecha = partes[2]
                    id_socio = int(partes[3])

                    nombre_clase = "Desconocida"
                    for clase in clases:
                        if clase["IdClase"] == id_clase:
                            nombre_clase = clase["NombreClase"]
                            break

                    nombre_socio = "Desconocido"
                    for socio in socios:
                        if socio["IdSocio"] == id_socio:
                            nombre_socio = f"{socio['Nombre']} {socio['Apellido']}"
                            break

                    fila = [
                        id_asistencia.center(20),
                        nombre_clase.center(20),
                        fecha.center(20),
                        nombre_socio.center(20)
                    ]
                    print(" | ".join(fila))
                    hay_asistencias = True

                linea = archivoA.readline()

            if not hay_asistencias:
                print("No hay asistencias registradas.")

        input("\nPresione una tecla para continuar...")
    
    except (FileNotFoundError, OSError) as error:
        print(f"Error! {error}")
        input("Presione una tecla para continuar...")
