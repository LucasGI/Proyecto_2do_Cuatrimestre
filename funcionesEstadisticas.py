from datos import socios, clases, asistencias, instructores


def promedioActivosInactivos():
    activos = sum(1 for socio in socios if socio.get('Activo', '').lower() == 'activo')
    inactivos = sum(1 for socio in socios if socio.get('Activo', '').lower() != 'activo')
    total = len(socios)
    promedioActivos= lambda activos, total: (activos / total * 100) 
    promedioInactivos= lambda inactivos, total: (inactivos / total * 100)

    print(f"Total de Socios: {total}")
    print(f"Socios Activos: {promedioActivos(activos, total)}%")
    print(f"Socios Inactivos: {promedioInactivos(inactivos, total)}%")
    input("Presione Enter para continuar...")


def cantidadSociosPorAbono():
    efectivo = sum(1 for socio in socios if socio.get('TipoAbono', '').lower() == 'efectivo')
    transferencia = sum(1 for socio in socios if socio.get('TipoAbono', '').lower() == 'transferencia')
    
    print(f"Socios con abono en Efectivo: {efectivo}")
    print(f"Socios con abono por Transferencia: {transferencia}")
    input("Presione Enter para continuar...")

def cantidadAsistenciaPorClase():
    clase_asistencia = {}
    for asistencia in asistencias:
        id_clase = asistencia["IdClase"]
        if id_clase in clase_asistencia:
            clase_asistencia[id_clase] += 1
        else:
            clase_asistencia[id_clase] = 1

    print("Promedio de asistencias por clase:")
    for clase in clases:
        id_clase = clase["IdClase"]
        nombre_clase = clase["NombreClase"]
        total_asistencias = clase_asistencia.get(id_clase, 0)
        print(f"Clase: {nombre_clase} - Total Asistencias: {total_asistencias}")
        input("Presione Enter para continuar...")

def cantidadClasesInstructor():
    instructor_clases = {}
    for clase in clases:
        id_instructor = clase["IdInstructor"]
        if id_instructor in instructor_clases:
            instructor_clases[id_instructor] += 1
        else:
            instructor_clases[id_instructor] = 1

    print("Cantidad de clases por instructor:")
    for instructor in instructores:
        id_instructor = instructor["IdInstructor"]
        nombre_instructor = f"{instructor['Nombre']} {instructor['Apellido']}"
        total_clases = instructor_clases.get(id_instructor, 0)
        print(f"Instructor: {nombre_instructor} - Total Clases: {total_clases} " )
    input("Presione Enter para continuar...")

