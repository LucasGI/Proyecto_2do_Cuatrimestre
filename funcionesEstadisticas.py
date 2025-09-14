from datos import socios, clases, asistencias, instructores

def promedioAsistenciaPorClase():
    # Contar asistencias por clase
    asistencia_por_clase = {}
    for asistencia in asistencias:
        id_clase = asistencia['id_clase']
        asistencia_por_clase[id_clase] = asistencia_por_clase.get(id_clase, 0) + 1

    # Lambda para calcular el promedio
    calcular_promedio = lambda total, alumnos: total / alumnos if alumnos > 0 else 0

    # Crear lista de tuplas (nombre_clase, promedio_asistencia)
    promedios = []
    for clase in clases:
        id_clase = clase['id']
        nombre_clase = clase['nombre']
        total_asistencias = asistencia_por_clase.get(id_clase, 0)
        cantidad_alumnos = len(clase['alumnos']) if 'alumnos' in clase else 1
        promedio = calcular_promedio(total_asistencias, cantidad_alumnos)
        promedios.append((nombre_clase, promedio))

    return promedios

def cantidadSociosActivosInactivos():
    activos = sum(1 for socio in socios if socio.get('Activo', False))
    inactivos = sum(1 for socio in socios if not socio.get('Activo', False))
    return activos, inactivos