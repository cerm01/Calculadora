import os

def captura():
    programadores = list()
    operaciones = list()
    primerosperandos = list()
    segundosoperandos = list()
    tme.s = list()
    Ids = list()
    x = 1
    y = 1
    #Limpiar pantalla
    os.system("cls")
    
    while x != 0:
        while y != 0:
            programador = input("Nombre del programador: ")
            operacion = input("Operación: ")
            primeroperando = int(input("Primer operando: "))
            segundooperando = int(input("Segundo operando: "))
            tme = int(input("Tiempo de ejecución: "))
            Id = int(input("Id: "))

            if validacion(operacion, segundooperando, tme, Id, Ids) == 0:
                programadores.append(programador)
                operaciones.append(operacion)
                primerosperandos.append(primeroperando)
                segundosoperandos.append(segundooperando)
                tme.s.append(tme)
                Ids.append(Id)
            else: 
                print("No se agregó el proceso") 
                
        x = int(input("¿Desea capturar otro proceso? 1.- Si 2.- No: "))
        if x == 1:
            pass
        elif x == 2:
            x = 0
        else:
            print("Opción no válida")
            x = 0


def validacion(operacion, segundooperando, tme, Id, Ids):
    valor = 0
    if operacion != ("+" or "-" or "*" or "/" or "//" or "**"):
        print("Operación no válida")
        valor += 1

    if operacion == ("/" or "//") and segundooperando == 0:
        print("No se puede dividir entre 0")
        valor += 1

    if tme < 1:
        print("El tiempo de ejecución debe ser mayor a 0")
        valor += 1
    
    for i in range(0, len(Ids)):
        if Id[i] == Id:
            print("El Id ya existe")
            valor += 1

    return valor


def menu():
    print("1.- Capturar procesos")
    print("2.- Procesar lotes")


def main():
    menu()
    opcion = int(input("Seleccione una opción: "))
    if opcion == 1:
        captura()
    elif opcion == 2:
        pass
    else:
        print("Opción no válida")


if __name__ == '__main__':
    main()