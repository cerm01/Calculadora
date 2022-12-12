

import os

def menu():
    print("1.- Capturar")
    print("2.- Procesar")

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
    bandera_captura = False

    opcion = 0

    while opcion != 2:
        menu()
        opcion = input("Seleccione una opción: ")
        opcion = validacion_menu(opcion)
        if opcion == 1:
            os.system("cls")
            captura(operaciones, primerosperandos, segundosoperandos, tmes, Ids, tt_list, bandera_resultado, tr_list)
            bandera_captura = True
        elif opcion == 2 and bandera_captura == True:
            os.system("cls")
            procesar(operaciones, primerosperandos, segundosoperandos, tmes, Ids, bandera_resultado, tt_list, tr_list)
        elif opcion == 2 and bandera_captura == False:
            print("No se ha capturado")
            os.system("pause")
            os.system("cls")
        else:
            print("Opción no válida")
            os.system("pause")
            os.system("cls")


if __name__ == '__main__':
     main()