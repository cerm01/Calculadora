def validacion(operacion, segundooperando, tme, Id, Ids):
    valor = 0
    if operacion == "+" or operacion == "-" or operacion == "*" or operacion == "/" or operacion == "%" or operacion =="**":
        pass
    else:
        valor += 1

    if (operacion == "/" or operacion == "%") and segundooperando == 0:
        valor += 1

    if tme < 1:
        valor += 1
    
    for i in range(0, len(Ids)):
        if Ids[i] == Id:
            valor += 1

    return valor