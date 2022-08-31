import os

def captura():
    programadores = list()
    operaciones = list()
    primerosperando = list()
    segundosoperando = list()
    tme = list()
    Id = list()
    x = 1
    y = 1
    #Limpiar pantalla
    os.system("cls")
    
    while x != 1:
        while y != 0:
            programador = input("Nombre del programador: ")
            operacion = input("Operación: ")
            primeroperando = int(input("Primer operando: "))
            segundooperando = int(input("Segundo operando: "))
            tme = int(input("Tiempo de ejecución: "))
            Id = int(input("Id: "))
            if validacion(operacion, primeroperando, segundooperando, tme, Id) == 0:
                y = 0     
            else:
                programadores.append(programador)
                operaciones.append(operacion)
                primerosperando.append(primeroperando)
                segundosoperando.append(segundooperando)
                tme.append(tme)
                Id.append(Id)
                
        x = int(input("¿Desea capturar otro proceso? 1.- Si 2.- No: "))


def validacion(operacion, segundooperando, tme, Id):
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
    
    for i in range(len(Id)):
        if Id[i] == Id:
            print("El Id ya existe")
            valor += 1

    return valor


def menu():
    print("1.- Capturar procesos")
    print("2.- Procesar lotes")


def main():
    pass


if __name__ == '__main__':
    main()