from math import trunc

def operacion(operacion, primeroperando, segundooperando):
    if operacion == "+":
        return primeroperando + segundooperando
    elif operacion == "-":
        return primeroperando - segundooperando
    elif operacion == "*":
        return primeroperando * segundooperando
    elif operacion == "/":
        return trunc((primeroperando / segundooperando)*1000)/1000
    elif operacion == "%":
        return trunc((primeroperando % segundooperando)*1000)/1000
    elif operacion == "**":
        return primeroperando ** segundooperando