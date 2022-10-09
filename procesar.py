from operacion import operacion
import os
import time
import keyboard

def procesar(operaciones, primerosperandos, segundosoperandos, tmes, Ids, bandera_resultado, tt_list, tr_list):
    nuevos = list()
    listo = list()
    bloqueado = list()
    finalizados = list()

    contador_global = 0 
    last = 0

    for i in range(0, len(Ids)):
        nuevos.append(Ids[i]-1)  

    for j in range(0, 3):
        listo.append(nuevos[0])
        nuevos.pop(0)

    while len(nuevos) > 0: 
        
        for i in range(0, len(listo)+1):
            ejecucion = listo.pop(0)
            while tt_list[ejecucion] < tmes[ejecucion]:
                tt_list[ejecucion] += 1
                tr_list[ejecucion] = tmes[ejecucion] - tt_list[ejecucion]
                contador_global += 1
                os.system("cls")
                imprimir(nuevos, listo, ejecucion, finalizados, Ids, tmes, primerosperandos, operaciones, segundosoperandos, bandera_resultado, tt_list, contador_global, tr_list, last)
                
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
                        imprimir(nuevos, listo, ejecucion, finalizados, Ids, tmes, primerosperandos, operaciones, segundosoperandos, bandera_resultado, tt_list, contador_global, tr_list, last)
                        if keyboard.is_pressed('c' or 'C'):
                            break

            finalizados.append(ejecucion)
            if len(nuevos) > 0:
                listo.append(nuevos.pop(0))
            

    last = 1
    os.system("cls")        
    imprimir(nuevos, listo, ejecucion, finalizados, Ids, tmes, primerosperandos, operaciones, segundosoperandos, bandera_resultado, tt_list, contador_global, tr_list, last)
    os.system("pause")


def imprimir(nuevos, listo, ejecucion, finalizados, Ids, tmes, primerosperandos, operaciones, segundosoperandos, bandera_resultado, tt_list, contador_global, tr_list, last):
    print("Procesos pendientes: ", len(nuevos) ) 
    print("")
    print("-----------------")
    print("Listos")
    print("-----------------")
    print("")
    j = 0
    for j in range (0, len(listo)):
        print("ID: ", Ids[listo[j]], "\t", "TME: ", tmes[listo[j]], "\t", "TT: ", tt_list[listo[j]], "\t", "TR: ", tr_list[listo[j]])

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
    j = 0
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
