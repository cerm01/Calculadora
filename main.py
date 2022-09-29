import os
import random
import time
import keyboard

def menu():
    print("1.- Capturar procesos")
    print("2.- Procesar lotes")

def validacion_menu(opcion):
    if opcion.isnumeric() == False:
        opcion = 0
        print("Opción no válida")
        os.system("pause")
        os.system("cls")
    else:
        opcion = int(opcion)
    
    return opcion 


def main():   
    from captura import captura
    from procesar import procesar

    operaciones = list()
    primerosperandos = list()
    segundosoperandos = list()
    tmes = list()
    tt_list = list()
    tr_list = list()
    Ids = list()
    bandera_resultado = list()
    num_lotes = 0
    

    opcion = 0
    

    while opcion != 2:
        menu()
        opcion = input("Seleccione una opción: ")
        opcion = validacion_menu(opcion)
        if opcion == 1:
            os.system("cls")
            captura(operaciones, primerosperandos, segundosoperandos, tmes, Ids, num_lotes, tt_list, bandera_resultado)
        elif opcion == 2:
            os.system("cls")
            procesar(operaciones, primerosperandos, segundosoperandos, tmes, Ids, bandera_resultado, tt_list, tr_list)
        else:
            print("Opción no válida")
            os.system("pause")
            os.system("cls")


if __name__ == '__main__':
    main()