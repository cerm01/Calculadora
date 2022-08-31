import os

def captura(programadores, operaciones, primerosperandos, segundosoperandos, tmes, Ids):
    x = 1
    y = 1
        
    while x != 0:
        print("Captura de procesos")
        while y != 0:
            programador = input("Nombre del programador: ")
            print("Operaciones validas : +, -, *, /, //, **")
            operacion = str(input("Operación: "))
            primeroperando = int(input("Primer operando: "))
            segundooperando = int(input("Segundo operando: "))
            tme = int(input("Tiempo de ejecución: "))
            Id = int(input("Id: "))
            os.system("cls")

            if validacion(operacion, segundooperando, tme, Id, Ids) == 0:
                programadores.append(programador)
                operaciones.append(operacion)
                primerosperandos.append(primeroperando)
                segundosoperandos.append(segundooperando)
                tmes.append(tme)
                Ids.append(Id)
                y = 0
            else: 
                print("No se agregó el proceso")
                os.system("pause")
                os.system("cls")
                
        x = int(input("¿Desea capturar otro proceso? 1.- Si 2.- No: "))
        if x == 1:
            y = 1
        elif x == 2:
            x = 0
        else:
            print("Opción no válida")
            os.system("pause")
            x = 0
        os.system("cls")


def validacion(operacion, segundooperando, tme, Id, Ids):
    valor = 0
    if operacion == "+" or operacion == "-" or operacion == "*" or operacion == "/" or operacion == "//" or operacion =="**":
        pass
    else:
        print("Operación no válida")
        valor += 1

    if (operacion == "/" or operacion == "//") and segundooperando == 0:
        print("No se puede dividir entre 0")
        valor += 1

    if tme < 1:
        print("El tiempo de ejecución debe ser mayor a 0")
        valor += 1
    
    for i in range(0, len(Ids)):
        if Ids[i] == Id:
            print("El Id ya existe")
            valor += 1

    return valor


def procesar(programadores, operaciones, primerosperandos, segundosoperandos, tmes, Ids):
    pass


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
    programadores = list()
    operaciones = list()
    primerosperandos = list()
    segundosoperandos = list()
    tmes = list()
    Ids = list()
    opcion = 0

    while opcion != 2:
        menu()
        opcion = input("Seleccione una opción: ")
        opcion = validacion_menu(opcion)
        if opcion == 1:
            os.system("cls")
            captura(programadores, operaciones, primerosperandos, segundosoperandos, tmes, Ids)
        elif opcion == 2:
            os.system("cls")
            procesar(programadores, operaciones, primerosperandos, segundosoperandos, tmes, Ids)
        else:
            print("Opción no válida")
            os.system("pause")
            os.system("cls")


if __name__ == '__main__':
    main()