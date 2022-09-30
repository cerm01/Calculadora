from operacion import operacion
import os
import time
import keyboard

def procesar(operaciones, primerosperandos, segundosoperandos, tmes, Ids, bandera_resultado, tt_list, tr_list):
    nuevos = list()
    listo = list()
    bloqueado = list()
    finalizados = list()

    lotes = 0
    acumulador = 0
    contador_global = 0
    cont_lotes = 0
    x = 0  
    cont = 0
    last = 0

    for i in range(0, len(Ids)):
        nuevos.append(Ids[i])

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
                listo.append(j)
            if cont == 3:
                cont = 0
                x = j + 1
                break
        
        cont_lotes += 1
        for i in range(0, len(listo)):
            ejecucion = listo.pop(0)
            while tt_list[ejecucion] < tmes[ejecucion]:
                tt_list[ejecucion] += 1
                tr_list[ejecucion] = tmes[ejecucion] - tt_list[ejecucion]
                contador_global += 1
                os.system("cls")
                imprimir(lotes, cont_lotes, listo, ejecucion, finalizados, Ids, tmes, primerosperandos, operaciones, segundosoperandos, bandera_resultado, tt_list, contador_global, tr_list, last)
                
                print("")
                
                if keyboard.is_pressed('e' or 'E'):
                    os.system("cls")
                    listo.append(ejecucion)
                    ejecucion = listo.pop(0)


                if keyboard.is_pressed('w' or 'W'):
                    os.system("cls")
                    bandera_resultado[ejecucion] = 1
                    
                    break

                if keyboard.is_pressed('p' or 'P'):
                    while True:
                        os.system("cls")
                        contador_global += 1
                        imprimir(lotes, cont_lotes, listo, ejecucion, finalizados, Ids, tmes, primerosperandos, operaciones, segundosoperandos, bandera_resultado, tt_list, contador_global, tr_list, last)
                        if keyboard.is_pressed('c' or 'C'):
                            break

            finalizados.append(ejecucion)

    last = 1
    os.system("cls")        
    imprimir(lotes, cont_lotes, listo, ejecucion, finalizados, Ids, tmes, primerosperandos, operaciones, segundosoperandos, bandera_resultado, tt_list, contador_global, tr_list, last)
    os.system("pause")


def imprimir(lotes, cont_lotes, listo, ejecucion, finalizados, Ids, tmes, primerosperandos, operaciones, segundosoperandos, bandera_resultado, tt_list, contador_global, tr_list, last):
    print("Lotes pendientes: ", lotes - cont_lotes)
    print("")
    print("-----------------")
    print("Listos")
    print("-----------------")
    print("")
    for i in range (0, len(listo)):
        print("ID: ", Ids[listo[i]], "\t", "TME: ", tmes[listo[i]], "\t", "TT: ", tt_list[listo[i]], "\t", "TR: ", tr_list[listo[i]])

    if last != 1:
        print("")
        print("--------------------")
        print("Ejecución")
        print("--------------------")
        print("")
        print("Operacion: ", primerosperandos[ejecucion], operaciones[ejecucion], segundosoperandos[ejecucion])
        print("ID: ", Ids[ejecucion])
        print("TME: ", tmes[ejecucion])
        print("TT: ", tt_list[ejecucion])
        print("TR: ", tr_list[ejecucion])
    else: 
        print("")
        print("--------------------")
        print("Ejecución")
        print("--------------------")
        print("")
    
    print("")
    print("-------------------")
    print("Finalizados")
    print("-------------------")
    print("")
    for j in range(0, len(finalizados)):
        print("ID: ", Ids[finalizados[j]], "", "\t", "Operacion: ", primerosperandos[finalizados[j]], operaciones[finalizados[j]], segundosoperandos[finalizados[j]], "\t", end="")
        
        if(bandera_resultado[finalizados[j]] == 0):
            print("Resultado: ", operacion(operaciones[finalizados[j]], primerosperandos[finalizados[j]], segundosoperandos[finalizados[j]]))
        if bandera_resultado[finalizados[j]] == 1:
            print("Resultado: ERROR")
    print("")
    print("Tiempo total de ejecución: ", contador_global)
    print("")
    time.sleep(1)
