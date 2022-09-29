from main import main

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