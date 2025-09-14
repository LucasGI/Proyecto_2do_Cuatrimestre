from datos import socios, clases, asistencias, instructores

def promedioAsistenciaPorClase():
    # Contar asistencias por clase
    asistencia_por_clase = {}
    for asistencia in asistencias:
        id_clase = asistencia['IdClase']
        asistencia_por_clase[id_clase] = asistencia_por_clase.get(id_clase, 0) + 1

    # Lambda para calcular el promedio
    calcular_promedio = lambda total, alumnos: total / alumnos if alumnos > 0 else 0

    # Crear lista de tuplas (NombreClase, promedio_asistencia)
    promedios = []
    for clase in clases:
        id_clase = clase['IdClase']
        nombre_clase = clase['NombreClase']
        # No hay campo 'alumnos', así que se asume 1 para evitar división por cero
        cantidad_alumnos = 1
        total_asistencias = asistencia_por_clase.get(id_clase, 0)
        promedio = calcular_promedio(total_asistencias, cantidad_alumnos)
        promedios.append((nombre_clase, promedio))

    return promedios

def cantidadSociosActivosInactivos():
    activos = sum(1 for socio in socios if socio.get('Activo', '').lower() == 'activo')
    inactivos = sum(1 for socio in socios if socio.get('Activo', '').lower() != 'activo')
    return activos, inactivos