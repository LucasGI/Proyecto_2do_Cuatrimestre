from funciones import *
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
                    id_instructor = input("Introduce el ID instructore: ")
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

                elif op == "0":
                    flag_seguir = False

            else:
                flag_seguir = False
                flagIn = False
                print("Gracias por usar el programa, saliendo...")










main()

    
   