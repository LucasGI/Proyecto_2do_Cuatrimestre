encabezados_socios = ['IdSocio','Nombre', 'Apellido', 'FechaNac', 'TipoAbono', 'EstadoPago', 'Activo']
socios=[
    ['1', 'Pepe', 'Juarez', '25/03/1998', 'Efectivo', 'Pago', 'Activo' ],
    ['2', 'Juan', 'Gonzalez', '12/09/2001', 'Transferencia', 'NoPago', 'Activo' ],
    ['3', 'Malena', 'Varela', '17/11/1996', 'Efectivo', 'Pago', 'Activo' ],
    ['4', 'Lucas', 'Rodriguez', '05/05/1985', 'Transferencia', 'NoPago', 'Activo' ],
    ['5', 'Emanuel', 'Gomez', '11/12/2005', 'Efectivo', 'Pago', 'Activo' ]
]

encabezados_clases = ['IdClase', 'NombreClase', 'Dia', 'Hora', 'IdInstructor', 'Activo']
clases=[
    ['1', 'Musculacion', 'Martes', '18:00', '1', 'Activo'],
    ['2', 'Zumba', 'Viernes', '19:00', '2', 'Activo'],
    ['3', 'Spinning', 'Lunes', '20:00', '3', 'Activo'],
    ['4', 'Funcional', 'Jueves', '13:00', '4', 'Activo'],
    ['5', 'Pilates', 'Miercoles', '09:00', '5', 'Activo']
]

encabezados_asistencias =  ['IdAsistencia', 'IdSocio', 'Fecha', 'IdClase']
asistencias=[
    ['1', '2', '13/09/25', '3'],
    ['2', '1', '23/05/25', '1'],
    ['3', '3', '05/12/25', '2'],
    ['4', '5', '27/11/25', '4'],
    ['5', '4', '11/03/25', '5']
]

encabezados_instructores = ['IdInstructor', 'Nombre', 'Apellido', 'FechaNac', 'Activo']
instructores=[
    ['1', 'Mateo', 'Perez','25/03/1998', 'Activo'],
    ['2', 'Joaquin', 'Lopez','12/09/2001', 'Activo'],
    ['3', 'Nicolas', 'Fernandez', '17/11/1996', 'Activo'],
    ['4', 'Ana', 'Diaz', '05/05/1985', 'Activo'],
    ['5', 'Luis', 'Sanchez', '11/12/2005', 'Activo']

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

def crearClases(clases):
    print("\n=== Crear Clase ===")
    idClase = str(len(clases)+1)  # esto genera el id dde clase
    nombreClase = input("Ingrese el nombre de la clase: ")
    dia = input("Ingrese el dia de la clase: ")
    hora = input("Ingrese la hora de la clase: ")
    idInstructor = input("Ingrese el ID del instructor: ")

    nuevo = [idClase,  nombreClase, dia, hora, idInstructor, "Activo"]
    clases.append(nuevo)
    print("Clase agregada con exito. ")

def mostrarClases(clases):
    print(" | ".join([e.center(15) for e in encabezados_clases]))
    print("-" * (len(encabezados_clases) * 18)) 
    for i in clases:
        if i[-1] == "Activo":
            print(" | ".join([dato.center(15) for dato in i]))

def editarClases(listaClases, idClase):
    
    for fila in listaClases:
        
        if fila[0] == idClase and fila[-1] == "Activo":
            
            nombre = input("Ingrese el nuevo nombre de la clase: ")
            dia = input("Ingrese el dia de la clase: ")
            
            hora = input("Ingrese la hora de la clase: ")
            idInstructor = input("Ingrese el ID del instructor: ")

            fila[1], fila[2], fila[3], fila[4] = nombre, dia, hora, idInstructor
            
            return "Clase modificada con exito. "
    print("Clase no encontrada. ")

def darBajaClase(listaClases, idClase):
    for clase in listaClases:
        if clase[0] == str(idClase):  
            clase[-1] = "Inactivo"                                             #///////VALIDAR QUE LA CLASE ESTE ACTIVA///////
            return f"Clase {clase[1]} {clase[2]} dada de baja."
    print("Clase no encontrada.")

def crearInstructor(instructores):
    print("\n=== Crear Instructor ===")
    idInstructor = str(len(instructores)+1)  # esto genera el id del socio
    nombre = input("Ingrese el nombre: ")
    apellido = input("Ingrese el apellido: ")
    fechaNac = input("Ingrese la fecha de nacimiento: ")

    nuevo = [idInstructor,  nombre, apellido, fechaNac, "Activo"]
    instructores.append(nuevo)
    print("Instructor agregado con exito. ")

def darBajaInstructor(listaInstructores, idInstructor):
    for instructor in listaInstructores:
        if instructor[0] == str(idInstructor):  
            instructor[-1] = "Inactivo"                                             #///////VALIDAR QUE EL Instructor este activo///////
            return f"Instructor {instructor[1]} {instructor[2]} dado de baja."
    print("Instructor no encontrado.")

def mostrarInstructores(instructores):
    print(" | ".join([e.center(15) for e in encabezados_instructores]))
    print("-" * (len(encabezados_instructores) * 18)) 
    for i in instructores:
        if i[-1] == "Activo":
            print(" | ".join([dato.center(15) for dato in i]))

def editarInstructor(listaInstructores, idInstructor):
    
    for fila in listaInstructores:
        
        if fila[0] == idInstructor and fila[-1] == "Activo":
            
            nombre = input("Ingrese el nuevo nombre: ")
            apellido = input("Ingrese el nuevo apellido: ")
            
            fechaNac = input("Ingrese fecha de nacimiento: ")

            fila[1], fila[2], fila[3] = nombre, apellido, fechaNac
            
            return "modificado con exito. "
    print("Instructor no encontrado. ")

def darBajaInstructor(listaInstructores, idInstructor):
    for instructor in listaInstructores:
        if instructor[0] == str(idInstructor):  
            instructor[-1] = "Inactivo"                                             #///////VALIDAR QUE EL INSTRUCTOR ESTE ACTIVO///////
            return f"Instructor {instructor[1]} {instructor[2]} dado de baja."
    print("Instructor no encontrado.")


# Funcion para logearse, si la contraseña es incorrecta no entrara al menu de administrador
def log_in():
    clear()
    print("\n=== Login ===")
    intentos = 3
    while intentos > 0:
        password = input("Ingrese la contraseña: ")
        if password == "admin123":
            print("Login exitoso.")
            return True
        else:
            intentos -= 1
            clear()
            print(f"Contraseña incorrecta. Le quedan ", intentos, " intentos")
    print("Ha agotado los intentos. Volviendo al menú principal.")
    return False
