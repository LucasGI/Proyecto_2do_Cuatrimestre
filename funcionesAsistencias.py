from datos import socios, clases, asistencias, instructores
from funcionesValidacion import clear, validarOpcion, validarClase, validarSocio

#--------------------- Funciones relacionadas a la entidad Asistencias ------------------------


def crearAsistencias(asistencia):
    print("\n=== Crear asistencia ===")
    id_asistencia = str(len(asistencia) + 1)
    id_socio = input("Ingrese el id del socio: ")
    id_clase = input("Ingrese el ID de la clase: ")
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


