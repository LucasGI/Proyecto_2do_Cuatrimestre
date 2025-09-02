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
                    id_socio = input("Introduce el ID socio: ")
                    darBajaSocio(socios, id_socio)
                elif op == "3":
                    op = menuEdicionSocios()
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
                    id_instructor = input("Introduce el ID instructore: ")
                    darBajaInstructor(instructores, id_instructor)
                elif op == "3":
                    id_instructor = input("Introduce el ID instructore: ")
                    editarInstructor(instructores, id_instructor)
                elif op == "4":
                    mostrarInstructores(instructores)
                    input("Presiones una tecla para continuar...")
                elif op == "0":
                    flag_seguir = False
            elif op == "3":
                op = menuClases()
                if op == "1":
                    crearClases(clases)
                elif op == "2":
                    id_clase = input("Introduce el ID clase: ")
                    darBajaClase(clases, id_clase)
                elif op == "3":
                    id_clase = input("Introduce el ID clase: ")
                    editarClases(clases, id_clase)
                elif op == "4":
                    mostrarClases(clases)
                    input("Presiones una tecla para continuar...")
                elif op == "0":
                    flag_seguir = False

            else:
                flag_seguir = False
                flagIn = False
                print("Gracias por usar el programa, saliendo...")










main()

    
   