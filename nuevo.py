from validacion import validacion

import random

def nuevo(operaciones, primerosperandos, segundosoperandos, tmes, Ids, tt_list, bandera_resultado, tr_list):

    y = 1

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
        
        if operacion == "**":
            primeroperando = random.randint(1,6)
            segundooperando = random.randint(1,6)
        else:
            primeroperando = random.randint(0,100)
            segundooperando = random.randint(0,100)
        tme = random.randint(6,16)
        Id = len(Ids) + 1
        
        
        if validacion(operacion, segundooperando, tme, Id, Ids) == 0:
            operaciones.append(operacion)
            primerosperandos.append(primeroperando)
            segundosoperandos.append(segundooperando)
            tmes.append(tme)
            Ids.append(Id)
            y = 0

            tt_list.append(0)
            tr_list.append(0)
            bandera_resultado.append(-1)


