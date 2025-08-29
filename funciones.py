
encabezados_socios = ['IdSocio', 'Nombre', 'Apellido', 'FechaNac', 'TipoAbono', 'EstadoPago', 'Activo']
socios = [
    ['1', 'Damiano', 'David', '25/03/1998', 'Efectivo', 'Pago', 'Activo'],
    ['2', 'Anibal', 'Pachano', '12/09/2001', 'Transferencia', 'NoPago', 'Activo'],
    ['3', 'Malena', 'Varela', '17/11/1996', 'Efectivo', 'Pago', 'Activo'],
    ['4', 'Lucas', 'Rodriguez', '05/05/1985', 'Transferencia', 'NoPago', 'Activo'],
    ['5', 'Emanuel', 'Gomez', '11/12/2005', 'Efectivo', 'Pago', 'Activo']
]

encabezados_clases = ['IdClase', 'NombreClase', 'Dia', 'Hora', 'IdInstructor', 'Activo']
clases = [
    ['1', 'Musculacion', 'Martes', '18:00', '1', 'Activo'],
    ['2', 'Zumba', 'Viernes', '19:00', '2', 'Activo'],
    ['3', 'Spinning', 'Lunes', '20:00', '3', 'Activo'],
    ['4', 'Funcional', 'Jueves', '13:00', '4', 'Activo'],
    ['5', 'Pilates', 'Miercoles', '09:00', '5', 'Activo']
]

encabezados_asistencias = ['IdAsistencia', 'IdSocio', 'Fecha', 'IdClase']
asistencias = [
    ['1', '2', '13/09/25', '3'],
    ['2', '1', '23/05/25', '1'],
    ['3', '3', '05/12/25', '2'],
    ['4', '5', '27/11/25', '4'],
    ['5', '4', '11/03/25', '5']
]

encabezados_instructores = ['IdInstructor', 'Nombre', 'Apellido']
instructores = [
    ['1', 'Jim', 'Morrison'],
    ['2', 'Lucas', 'Rodriguez'],
    ['3', 'Nicolas', 'Fernandez'],
    ['4', 'Ana', 'Diaz'],
    ['5', 'Luis', 'Sanchez']

]


def clear():
    print("\n" * 50)


def crearSocio(socios):
    print("\n=== Crear socio ===")
    id_socio = str(len(socios) + 1)  # esto genera el id del socio
    nombre = input("Ingrese el nombre: ")
    apellido = input("Ingrese el apellido: ")
    fecha = input("Ingrese la fecha de nacimiento: ")
    abono = input("Tipo de abono (Efectivo/Transferencia): ")
    estado = input("Estado del pago (Pago/NoPago): ")

    nuevo = [id_socio, nombre, apellido, fecha, abono, estado, "Activo"]
    socios.append(nuevo)
    print("Socio agregado con exito. ")


def darBajaSocio(listaSocios, idSocio):
    for socio in listaSocios:
        if socio[0] == str(idSocio):
            socio[-1] = "Inactivo"  # ///////VALIDAR QUE EL SOCIO ESTE ACTIVO///////
            return f"Socio {socio[1]} {socio[2]} dado de baja."
    print("Socio no encontrado.")


def mostrarSocios(socios):
    clear()
    print(" | ".join([e.center(15) for e in encabezados_socios]))
    print("-" * (len(encabezados_socios) * 18))
    for i in socios:
        print(" | ".join([dato.center(15) for dato in i]))
    input("\n\nPresione enter para continuar...")



def editarSocios(listaSocios, idSocio):
    for fila in listaSocios:

        if fila[0] == idSocio:

            op = menuEdicionSocios()

            if op == '1':
                nombre = input("Ingrese el nuevo nombre: ")
                fila[1] = nombre
            elif op == '2':
                apellido = input("Ingrese el nuevo apellido: ")
                fila[2] = apellido
            elif op == '3':
                abono = input("Ingrese el tipo de abono: ")
                fila[3] = abono
            elif op == '4':
                estado = input("Ingrese el estado del pago: ")
                fila[4] = estado
            elif op == '0':
                print("Saliendo del menu de edicion.")
                return
            else:
                print("Opcion no valida.")
                return

            return "modificado con exito. "
    print("socio no encontrado. ")



def crearClase(listaClase):
    print("\n=== Crear clase ===")
    id_clase = str(len(listaClase) + 1)  # esto genera el id del socio
    nombreClase = input("Ingrese el nombre de la clase: ")
    Dia= input("Ingrese el dia: ")
    Hora = input("Ingrese la hora: ")
    id_instructor = input("Ingrese el ID de instructor: ")

    nuevo = [id_clase, nombreClase, Dia, Hora, id_instructor]
    listaClase.append(nuevo)
    print("Clase creada con exito. ")

def mostrarClase(clases):
    clear()
    print(" | ".join([e.center(15) for e in encabezados_clases]))
    print("-" * (len(encabezados_clases) * 18))
    for i in clases:
        print(" | ".join([dato.center(15) for dato in i]))
    input("\n\nPresione enter para continuar...")

def darBajaClase(clases):
    print("\n=== Eliminar clase ===")
    id_clase = input("Ingrese el ID de la clase a eliminar: ")
    for clase in clases:
        if clase[0] == id_clase:
            clase[-1] = "Inactivo"
            print("Clase dada de baja con exito. ")
            return








