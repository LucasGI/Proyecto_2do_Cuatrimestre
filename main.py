from funcionesClases import *
from funcionesEstadisticas import *
from funcionesSocios import *
from funcionesValidacion import *
from funcionesInstructores import *
from funcionesAsistencias import *
from datos import socios, clases, asistencias, instructores
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
                    crearSocio(socios)
                elif op == "2":
                    op = menuAltaBaja()

                    if op == "1":
                        id_socio = input("Introduce el ID socio: ")
                        darAltaSocio(socios, id_socio)
                    elif op == "2":
                        id_socio = input("Introduce el ID socio: ")
                        darBajaSocio(socios, id_socio)
                    elif op == "0":
                        menuSocios()
                elif op == "3":
                    id_socio = input("Introduce el ID socio: ")
                    editarSocios(socios, id_socio)
                elif op == "4":
                    mostrarSocios(socios)
                elif op == "0":
                    flag_seguir = False

            elif op == "2":
                op = menuInstructores()
                if op == "1":
                    crearInstructor(instructores)
                elif op == "2":
                    op = menuAltaBaja()

                    if op == "1":
                        id_instructor = input("Introduce el ID instructor: ")
                        darAltaInstructor(instructores, id_instructor)
                    elif op == "2":
                        id_instructor = input("Introduce el ID instructor: ")
                        darBajaInstructor(instructores, id_instructor)
                    elif op == "0":
                        menuInstructores()

                elif op == "3":
                    id_instructor = input("Introduce el ID instructores: ")
                    editarInstructor(instructores, id_instructor)
                elif op == "4":
                    mostrarInstructores(instructores)
                elif op == "0":
                    flag_seguir = False

            elif op == "3":
                op = menuClases()
                if op == "1":
                    crearClases(clases)
                elif op == "2":
                    op = menuAltaBaja()

                    if op == "1":
                        id_clase = input("Introduce el ID clase: ")
                        darAltaClase(clases, id_clase)
                    elif op == "2":
                        id_instructor = input("Introduce el ID clase: ")
                        darBajaClase(clases, id_instructor)
                    elif op == "0":
                        menuClases()
                elif op == "3":
                    id_clase = input("Introduce el ID clase: ")
                    editarClases(clases, id_clase)
                elif op == "4":
                    mostrarClases(clases)
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

            else:
                flag_seguir = False
                flagIn = False
                print("Gracias por usar el programa, saliendo...")


main()


