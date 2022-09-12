import os
import time

def captura(programadores, operaciones, primerosperandos, segundosoperandos, tmes, Ids):
    x = 1
    y = 1
        
    while x != 0:
        print("Captura de procesos")
        while y != 0:
            programador = input("Nombre del programador: ")
            print("Operaciones validas : +, -, *, /, % , **")
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
    if operacion == "+" or operacion == "-" or operacion == "*" or operacion == "/" or operacion == "%" or operacion =="**":
        pass
    else:
        print("Operación no válida")
        valor += 1

    if (operacion == "/" or operacion == "%") and segundooperando == 0:
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


def operacion(operacion, primeroperando, segundooperando):
    if operacion == "+":
        return primeroperando + segundooperando
    elif operacion == "-":
        return primeroperando - segundooperando
    elif operacion == "*":
        return primeroperando * segundooperando
    elif operacion == "/":
        return primeroperando / segundooperando
    elif operacion == "%":
        return primeroperando % segundooperando
    elif operacion == "**":
        return primeroperando ** segundooperando


def procesar(programadores, operaciones, primerosperandos, segundosoperandos, tmes, Ids):
    lotes = 0
    acumulador = 0
    tt = 0
    tr = 0
    tme = 0

    contador_global = 0
    cont_lotes = 0
    x = 0  
    cont = 0
    lote_ejecucion = list()
    procesos_finalizados = list()

    for i in range(0, len(tmes)):
        tme += tmes[i]
    resultado = list()

    for i in range(0, len(Ids)): 
        acumulador += 1
        if acumulador == 3:
            lotes += 1
            acumulador = 0
        elif i == len(Ids) - 1 and acumulador != 0:
            lotes += 1   

    while cont_lotes < lotes: 
        for j in range(x, len(Ids)):
            cont += 1
            if cont <= 3:
                lote_ejecucion.append(j)
            if cont == 3:
                cont = 0
                x = j + 1
                break
        
        for i in range(0, len(lote_ejecucion)):
            proceso_ejecucion = lote_ejecucion.pop(0)
            tme = tmes[proceso_ejecucion]
            while tt <= tme:
                print("Lotes pendientes: ", lotes - cont_lotes)
                print("")
                print("-----------------")
                print("Lote en ejecución")
                print("-----------------")
                print("")
                for i in range (0, len(lote_ejecucion)):
                    print("Programador", programadores[lote_ejecucion[i]] ,"\t","ID: ", Ids[lote_ejecucion[i]], "\t", "TME: ", tmes[lote_ejecucion[i]])

                print("")
                print("--------------------")
                print("Proceso en ejecución")
                print("--------------------")
                print("")
                print("Programador: ", programadores[proceso_ejecucion])
                print("Operacion: ", primerosperandos[proceso_ejecucion], operaciones[proceso_ejecucion], segundosoperandos[proceso_ejecucion])
                print("ID: ", Ids[proceso_ejecucion])
                print("TME: ", tmes[proceso_ejecucion])
                print("TT: ", tt)
                print("TR: ", tmes[proceso_ejecucion] - tt)
                
                print("")
                print("-------------------")
                print("Procesos finalizado")
                print("-------------------")
                print("")
                for j in range(0, len(procesos_finalizados)):
                    print("ID: ", Ids[procesos_finalizados[j]], "\t", "Operacion: ", primerosperandos[procesos_finalizados[j]], operaciones[procesos_finalizados[j]], segundosoperandos[procesos_finalizados[j]], "\t", "Resultado: ", operacion(operaciones[procesos_finalizados[j]], primerosperandos[procesos_finalizados[j]], segundosoperandos[procesos_finalizados[j]]))
                
                time.sleep(1)
                tt += 1
                contador_global += 1 
                os.system("cls")
                
            tt = 0
            procesos_finalizados.append(proceso_ejecucion)
            
        cont_lotes += 1            
    print("-----------------")
    print("Lote en ejecución")
    print("-----------------")

    print("--------------------")
    print("Proceso en ejecución")
    print("--------------------")

    print("-------------------")
    print("Procesos finalizado")
    print("-------------------")
    for j in range(0, len(procesos_finalizados)):
        print("ID: ", Ids[procesos_finalizados[j]], "\t", "Operacion: ", primerosperandos[procesos_finalizados[j]], operaciones[procesos_finalizados[j]], segundosoperandos[procesos_finalizados[j]], "\t", "Resultado: ", operacion(operaciones[procesos_finalizados[j]], primerosperandos[procesos_finalizados[j]], segundosoperandos[procesos_finalizados[j]]))
    print("")
    print("Tiempo total de ejecución: ", contador_global)
    os.system("pause")


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