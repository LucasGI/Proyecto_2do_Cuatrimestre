from funcionesClases import *
from funcionesEstadisticas import *
from funcionesSocios import *
from funcionesValidacion import *
from funcionesInstructores import *
from funcionesAsistencias import *
from datos import socios, clases, instructores
from menus import *


def main():
    flagIn = True
    log_in()

    while flagIn:
        flag_seguir = True

        while flag_seguir:
            op = menuPrincipal()

            if op == "1":
                op = menuSocios()
                if op == "1":
                    crearSocio("archivos/socios.json")
                elif op == "2":
                    op = menuAltaBaja()
                    if op == "1":
                        id_socio = int(input("Introduce el ID socio: "))
                        darAltaSocio("archivos/socios.json", id_socio)
                    elif op == "2":
                        id_socio = int(input("Introduce el ID socio: "))
                        darBajaSocio("archivos/socios.json", id_socio)
                    elif op == "0":
                        menuSocios()
                elif op == "3":
                    id_socio = int(input("Introduce el ID socio: "))
                    editarSocios("archivos/socios.json", id_socio)
                elif op == "4":
                    mostrarSocios("archivos/socios.json")
                elif op == "0":
                    flag_seguir = False

            elif op == "2":
                op = menuInstructores()
                if op == "1":
                    crearInstructor("archivos/instructores.json")
                elif op == "2":
                    op = menuAltaBaja()

                    if op == "1":
                        id_instructor = int(input("Introduce el ID instructor: "))
                        darAltaInstructor("archivos/instructores.json", id_instructor)
                    elif op == "2":
                        id_instructor = int(input("Introduce el ID instructor: "))
                        darBajaInstructor("archivos/instructores.json", id_instructor)
                    elif op == "0":
                        menuInstructores()

                elif op == "3":
                    id_instructor = int(input("Introduce el ID instructores: "))
                    editarInstructor("archivos/instructores.json", id_instructor)
                elif op == "4":
                    mostrarInstructores("archivos/instructores.json")
                elif op == "0":
                    flag_seguir = False

            elif op == "3":
                op = menuClases()
                if op == "1":
                    crearClases("archivos/clases.json")
                elif op == "2":
                    op = menuAltaBaja()
                    if op == "1":
                        id_clase = int(input("Introduce el ID clase: "))
                        darAltaClase("archivos/clases.json", id_clase)
                    elif op == "2":
                        id_instructor = int(input("Introduce el ID clase: "))
                        darBajaClase("archivos/clases.json", id_instructor)
                    elif op == "0":
                        menuClases()
                elif op == "3":
                    id_clase = int(input("Introduce el ID clase: "))
                    editarClases("archivos/clases.json", id_clase)
                elif op == "4":
                    op = menuMostrarClases()
                    if op == "1":
                        mostrarClases("archivos/clases.json")
                        
                    elif op == "2":
                        ordenarClasesPorHora("archivos/clases.json", False)
                
                    elif op == "3":
                        ordenarClasesPorHora("archivos/clases.json", True)
                    else:
                        op = input("Opcion no valida, reingrese: ")

            elif op == "5":
                op = menuEstadisticas()
                if op == "1":
                    cantidadSociosPorAbono()
                elif op == "2":
                    cantidadAsistenciaPorClase()
                elif op == "3": 
                    promedioActivosInactivos()
                elif op == "4": 
                    cantidadClasesInstructor()
            elif op == "4":
                op = menuAsistencias()
                if op == "1":
                    registrarAsistencia(asistencias, socios, clases)
                elif op == "2":
                    mostrarAsistencias(asistencias, socios, clases)
                elif op == "3":
                    id_asistencia = input("Introduce el ID de la asistencia a editar: ")
                    editarAsistencia(asistencias, id_asistencia)
                elif op == "4":
                    id_asistencia = input("Introduce el ID de la asistencia a anular: ")
                    anularAsistencia(asistencias, id_asistencia)
                elif op == "0":
                    flag_seguir = False
            elif op == "0":
                flag_seguir = False
                flagIn = False
                print("Gracias por usar el programa, saliendo...")

            else:
                op = input("Opcion no valida, reingrese: ")


main()


