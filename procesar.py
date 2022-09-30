from main import main
from operacion import operacion
import os

import time
import keyboard

def procesar(operaciones, primerosperandos, segundosoperandos, tmes, Ids, bandera_resultado, tt_list, tr_list):
    lotes = 0
    acumulador = 0
    tr = 0
    contador_global = 0
    cont_lotes = 0
    x = 0  
    cont = 0
    lote_ejecucion = list()
    procesos_finalizados = list()

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
        
        cont_lotes += 1
        for i in range(0, len(lote_ejecucion)):
            proceso_ejecucion = lote_ejecucion.pop(0)
            while tt_list[proceso_ejecucion] < tmes[proceso_ejecucion]:
                tt_list[proceso_ejecucion] += 1
                tr_list[proceso_ejecucion] = tmes[proceso_ejecucion] - tt_list[proceso_ejecucion]
                contador_global += 1
                os.system("cls")
                imprimir(lotes, cont_lotes, lote_ejecucion, proceso_ejecucion, procesos_finalizados, Ids, tmes, primerosperandos, operaciones, segundosoperandos, bandera_resultado, tt_list, contador_global, tr_list)
                
                print("")
                
                if keyboard.is_pressed('e' or 'E'):
                    os.system("cls")
                    lote_ejecucion.append(proceso_ejecucion)
                    proceso_ejecucion = lote_ejecucion.pop(0)


                if keyboard.is_pressed('w' or 'W'):
                    os.system("cls")
                    bandera_resultado[proceso_ejecucion] = 1
                    
                    break

                if keyboard.is_pressed('p' or 'P'):
                    while True:
                        os.system("cls")
                        contador_global += 1
                        imprimir(lotes, cont_lotes, lote_ejecucion, proceso_ejecucion, procesos_finalizados, Ids, tmes, primerosperandos, operaciones, segundosoperandos, bandera_resultado, tt_list, contador_global, tr_list)
                        if keyboard.is_pressed('c' or 'C'):
                            break

            procesos_finalizados.append(proceso_ejecucion)
                       
    imprimir(lotes, cont_lotes, lote_ejecucion, proceso_ejecucion, procesos_finalizados, Ids, tmes, primerosperandos, operaciones, segundosoperandos, bandera_resultado, tt_list, contador_global, tr_list)
    os.system("pause")


def imprimir(lotes, cont_lotes, lote_ejecucion, proceso_ejecucion, procesos_finalizados, Ids, tmes, primerosperandos, operaciones, segundosoperandos, bandera_resultado, tt_list, contador_global, tr_list):
    print("Lotes pendientes: ", lotes - cont_lotes)
    print("")
    print("-----------------")
    print("Lote en ejecución")
    print("-----------------")
    print("")
    for i in range (0, len(lote_ejecucion)):
        print("ID: ", Ids[lote_ejecucion[i]], "\t", "TME: ", tmes[lote_ejecucion[i]], "\t", "TT: ", tt_list[lote_ejecucion[i]], "\t", "TR: ", tr_list[lote_ejecucion[i]])

    print("")
    print("--------------------")
    print("Proceso en ejecución")
    print("--------------------")
    print("")
    print("Operacion: ", primerosperandos[proceso_ejecucion], operaciones[proceso_ejecucion], segundosoperandos[proceso_ejecucion])
    print("ID: ", Ids[proceso_ejecucion])
    print("TME: ", tmes[proceso_ejecucion])
    print("TT: ", tt_list[proceso_ejecucion])
    print("TR: ", tr_list[proceso_ejecucion])
    
    print("")
    print("-------------------")
    print("Procesos finalizado")
    print("-------------------")
    print("")
    for j in range(0, len(procesos_finalizados)):
        print("ID: ", Ids[procesos_finalizados[j]], "", "\t", "Operacion: ", primerosperandos[procesos_finalizados[j]], operaciones[procesos_finalizados[j]], segundosoperandos[procesos_finalizados[j]], "\t", end="")
        
        if(bandera_resultado[procesos_finalizados[j]] == 0):
            print("Resultado: ", operacion(operaciones[procesos_finalizados[j]], primerosperandos[procesos_finalizados[j]], segundosoperandos[procesos_finalizados[j]]))
        if bandera_resultado[procesos_finalizados[j]] == 1:
            print("Resultado: ERROR")
    print("")
    print("Tiempo total de ejecución: ", contador_global)
    print("")
    time.sleep(1)
