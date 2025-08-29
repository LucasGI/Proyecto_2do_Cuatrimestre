from funciones import *
from menus import *

def main():

    flagSeguir = True


    while flagSeguir:
        op = menuPrincipal()
        if op == "1":
            op = menuSocios()
            if op == "1":   
                crearSocio(socios)
            elif op == "2":
                darBajaSocio(socios)
            elif op == "3":
                editarSocios(socios)
            elif op == "4":
                mostrarSocios(socios)
            elif op == "0":
                break

        elif op == "2":
            '''Aca se invocan las funciones de instructores'''

        else:
            flagSeguir = False
            print("Gracias por usar el programa, saliendo...")










main()

    
   