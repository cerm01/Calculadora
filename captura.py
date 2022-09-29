
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