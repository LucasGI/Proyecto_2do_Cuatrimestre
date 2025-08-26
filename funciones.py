encabezados_socios = ['IdSocio','Nombre', 'Apellido', 'FechaNac', 'TipoAbono', 'EstadoPago', 'Activo']
socios=[
    ['1', 'Pepe', 'Juarez', '25/03/1998', 'Efectivo', 'Pago', 'Activo' ],
    ['2', 'Juan', 'Gonzalez', '12/09/2001', 'Transferencia', 'NoPago', 'Activo' ],
    ['3', 'Malena', 'Varela', '17/11/1996', 'Efectivo', 'Pago', 'Activo' ],
    ['4', 'Lucas', 'Rodriguez', '05/05/1985', 'Transferencia', 'NoPago', 'Activo' ],
    ['5', 'Emanuel', 'Gomez', '11/12/2005', 'Efectivo', 'Pago', 'Activo' ]
]

encabezados_clases = ['IdClase', 'NombreClase', 'Dia', 'Hora', 'IdInstructor']
clases=[
    ['1', 'Musculacion', 'Martes', '18:00', '1'],
    ['2', 'Zumba', 'Viernes', '19:00', '2'],
    ['3', 'Spinning', 'Lunes', '20:00', '3'],
    ['4', 'Funcional', 'Jueves', '13:00', '4'],
    ['5', 'Pilates', 'Miercoles', '09:00', '5']
]

encabezados_asistencias =  ['IdAsistencia', 'IdSocio', 'Fecha', 'IdClase']
asistencias=[
    ['1', '2', '13/09/25', '3'],
    ['2', '1', '23/05/25', '1'],
    ['3', '3', '05/12/25', '2'],
    ['4', '5', '27/11/25', '4'],
    ['5', '4', '11/03/25', '5']
]

encabezados_instructores = ['IdInstructor', 'Nombre', 'Apellido']
instructores=[
    ['1', 'Mateo', 'Perez'],
    ['2', 'Joaquin', 'Lopez'],
    ['3', 'Nicolas', 'Fernandez'],
    ['4', 'Ana', 'Diaz'],
    ['5', 'Luis', 'Sanchez']

]

def menusito():
    clear()
    print("\n=== Sistema de gestion Gym")
    print("1. Añadir usuario")
    print("2. Eliminar usuario")
    print("3. Modificar usuario")
    print("4. Mostrar usuarios")
    print("5. Salir")
    op = input("Seleccione una opcion: ")

    if op == "1":
        crearSocio()
    


def clear():
    print("\n" * 50)


def crearSocio(socios):
    print("\n=== Crear socio ===")
    id_socio = str(len(socios)+1)  # esto genera el id del socio
    nombre = input("Ingrese el nombre: ")
    apellido = input("Ingrese el apellido: ")
    fecha = input("Ingrese la fecha de nacimiento: ")
    abono = input("Tipo de abono (Efectivo/Transferencia): ")
    estado = input("Estado del pago (Pago/NoPago): ")

    nuevo = [id_socio,  nombre, apellido, fecha, abono, estado, "Activo"]
    socios.append(nuevo)
    print("Socio agregado con exito. ")


def darBajaSocio(listaSocios, idSocio):
    for socio in listaSocios:
        if socio[0] == str(idSocio):  
            socio[-1] = "Inactivo"                                             #///////VALIDAR QUE EL SOCIO ESTE ACTIVO///////
            return f"Socio {socio[1]} {socio[2]} dado de baja."
    print("Socio no encontrado.")


def mostrarSocios(socios):
    print(" | ".join([e.center(15) for e in encabezados_socios]))
    print("-" * (len(encabezados_socios) * 18)) 
    for i in socios:
        if i[-1] == "Activo":
            print(" | ".join([dato.center(15) for dato in i]))

def editarSocios(listaSocios, idSocio):
    
    
    for fila in listaSocios:
        
        if fila[0] == idSocio and fila[-1] == "Activo":
            
            nombre = input("Ingrese el nuevo nombre: ")
            apellido = input("Ingrese el nuevo apellido: ")
            
            abono = input("Tipo de abono (Efectivo/Transferencia): ")
            estado = input("Estado del pago (Pago/NoPago): ")

            fila[1], fila[2], fila[4], fila[5] = nombre, apellido, abono, estado
            
            return "modificado con exito. "
    print("socio no encontrado. ")


