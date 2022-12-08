from operacion import operacion
import os
import time
import keyboard

def procesar(operaciones, primerosperandos, segundosoperandos, tmes, Ids, bandera_resultado, tt_list, tr_list):
    nuevos = list()
    listo = list()
    bloqueado = list()
    finalizados = list()

    tiempo_bloqueado = list()

    contador_global = 0 
    last = 0

    #---------------------------------------------------------
    t_llegada = list()
    t_finalizacion = list()
    t_retorno = list()
    t_respuesta = list()
    t_espera = list()
    t_servicio = list()
    #---------------------------------------------------------
    for i in range(0, len(Ids)):
        t_llegada.append(-1)
        t_finalizacion.append(-1)
        t_retorno.append(-1)
        t_respuesta.append(-1)
        t_espera.append(-1)
        t_servicio.append(-1)
    #---------------------------------------------------------

    for i in range(0, len(Ids)):
        nuevos.append(Ids[i]-1)

    if len(nuevos) < 3:
        x = len(nuevos)
    else:
        x = 3  

    for j in range(0, x):
        listo.append(nuevos[0])
        nuevos.pop(0)
        if t_llegada[j] == -1:
            t_llegada[j] = contador_global

    while len(nuevos) + len(listo) + len(bloqueado) > 0: 
        
        for i in range(0, len(listo)):
            
            if len(listo) > 0:
                ejecucion = listo.pop(0)

            while tt_list[ejecucion] < tmes[ejecucion]:
                
                if t_respuesta[ejecucion] == -1:
                    t_respuesta[ejecucion] = contador_global
                
                contador_global += 1

                for j in range(0, len(bloqueado)):
                    tiempo_bloqueado[j] += 1
                
                if len(bloqueado) > 0:
                    if tiempo_bloqueado[0] == 7 and len(bloqueado) == 3:
                        listo.append(bloqueado[0])
                        ejecucion = listo[0]
                        listo.pop(0)
                        tiempo_bloqueado.pop(0)
                        bloqueado.pop(0)
                    elif tiempo_bloqueado[0] == 7 and len(bloqueado) < 3:
                        listo.append(bloqueado[0])
                        tiempo_bloqueado.pop(0)
                        bloqueado.pop(0)
                
                if len(bloqueado)< 3:
                    tt_list[ejecucion] += 1
                    tr_list[ejecucion] = tmes[ejecucion] - tt_list[ejecucion]

                os.system("cls")
                imprimir(nuevos, listo, ejecucion, finalizados, Ids, tmes, primerosperandos, operaciones, segundosoperandos, bandera_resultado, tt_list, contador_global, tr_list, last, tiempo_bloqueado, bloqueado)

                if keyboard.is_pressed('e' or 'E'):
                    if len(bloqueado)<3 and tr_list[ejecucion] > 0:
                        bloqueado.append(ejecucion)
                        tiempo_bloqueado.append(0)
                        if len(listo) > 0:
                            ejecucion = listo.pop(0)

                if keyboard.is_pressed ('w' or 'W'):
                    if (len(bloqueado) < 3) and (tr_list[ejecucion] > 0):
                        os.system("cls")
                        bandera_resultado[ejecucion] = 1
                    
                        break

                if keyboard.is_pressed ('p' or 'P'):
                    while True:
                        os.system("cls")
                        contador_global += 1
                        imprimir(nuevos, listo, ejecucion, finalizados, Ids, tmes, primerosperandos, operaciones, segundosoperandos, bandera_resultado, tt_list, contador_global, tr_list, last, tiempo_bloqueado, bloqueado)
                        if keyboard.is_pressed('c' or 'C'):
                            break

            finalizados.append(ejecucion)
            
            t_finalizacion[ejecucion] = contador_global
            t_retorno[ejecucion] = t_finalizacion[ejecucion] - t_llegada[ejecucion]
            t_espera[ejecucion] = t_respuesta[ejecucion] - t_llegada[ejecucion]
            t_servicio[ejecucion] = t_retorno[ejecucion] - t_espera[ejecucion]

            if len(nuevos) > 0:
                new = nuevos.pop(0)
                listo.append(new)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
                if t_llegada[new] == -1:
                    t_llegada[new] = contador_global
            elif len(nuevos) == 0 and len(bloqueado):
                ejecucion = bloqueado[0]
            

    last = 1
    os.system("cls")        
    imprimir(nuevos, listo, ejecucion, finalizados, Ids, tmes, primerosperandos, operaciones, segundosoperandos, bandera_resultado, tt_list, contador_global, tr_list, last, tiempo_bloqueado, bloqueado)
    os.system("pause")
    tiempos(Ids, tmes, primerosperandos, operaciones, segundosoperandos, t_llegada, t_finalizacion, t_retorno, t_respuesta, t_espera, t_servicio)
    os.system("pause")

def imprimir(nuevos, listo, ejecucion, finalizados, Ids, tmes, primerosperandos, operaciones, segundosoperandos, bandera_resultado, tt_list, contador_global, tr_list, last, tiempo_bloqueado, bloqueado):
    print("Procesos pendientes: ", len(nuevos) ) 
    print("")
    print("----------------- LISTOS -----------------")
    
    
    j = 0
    for j in range (0, len(listo)):
        print("ID: ", Ids[listo[j]], "\t", "TME: ", tmes[listo[j]], "\t", "TT: ", tt_list[listo[j]], "\t", "TR: ", tr_list[listo[j]])
    print("")
    print("----------------- EJECUCIÓN -----------------")
    
    if last != 1:
        if len(bloqueado) < 3:
            print("Operacion: ", primerosperandos[ejecucion], operaciones[ejecucion], segundosoperandos[ejecucion])
            print("ID: ", Ids[ejecucion])
            print("TME: ", tmes[ejecucion])
            print("TT: ", tt_list[ejecucion])
            print("TR: ", tr_list[ejecucion])

    print("")
    print("----------------- BLOQUEADOS -----------------")

    
    for k in range(0, len(bloqueado)):
        print("ID: ", Ids[bloqueado[k]], "\t", "Tiempo bloqueado: ", tiempo_bloqueado[k])

    print("")
    print("----------------- FINALIZADOS -----------------")
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

def tiempos(Ids, tmes, primerosperandos, operaciones, segundosoperandos, t_llegada, t_finalizacion, t_retorno, t_respuesta, t_espera, t_servicio):
    print("ID", "\t", "TME", "\t", "Operacion", "\t", "TLL", "\t", "TF", "\t", "TR", "\t", "RESP", "\t", "TE", "\t", "TS")
    for i in range(0, len(Ids)):
        print (Ids[i], "\t", tmes[i], "\t", primerosperandos[i], operaciones[i], segundosoperandos[i], "\t", t_llegada[i], "\t", t_finalizacion[i], "\t", t_retorno[i], "\t", t_respuesta[i], "\t", t_espera[i], "\t", t_servicio[i])