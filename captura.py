from main import main
from validacion import validacion

def captura(operaciones, primerosperandos, segundosoperandos, tmes, Ids, num_lotes, tt_list, bandera_resultado):

    print("Captura de procesos")
    print("")
    num_lotes = int(input("¿Cuántos lotes desea capturar? "))
    y = 1
    for i in range(0, num_lotes):
        
        while y != 0:
                       
            aleatorio = random.randint(1,6)
            if aleatorio == 1:
                operacion = "+"
            elif aleatorio == 2:
                operacion = "-"
            elif aleatorio == 3:
                operacion = "*"
            elif aleatorio == 4:
                operacion = "/"
            elif aleatorio == 5:
                operacion = "%"
            elif aleatorio == 6:
                operacion = "**"
            
            primeroperando = random.randint(0,100)
            segundooperando = random.randint(0,100)
            tme = random.randint(6,16)
            Id = i + 1
            
            
            if validacion(operacion, segundooperando, tme, Id, Ids) == 0:
                operaciones.append(operacion)
                primerosperandos.append(primeroperando)
                segundosoperandos.append(segundooperando)
                tmes.append(tme)
                Ids.append(Id)
                y = 0

            tt_list.append(0)
            bandera_resultado.append(0)
            
        y = 1
    os.system("cls")