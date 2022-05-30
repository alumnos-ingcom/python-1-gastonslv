################
# Gaston Silvestre - @gastonslv
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
5. Divisiones
"""

from ejercicio2 import signo

def division_lenta(dividendo, divisor):

    ## ENTRADA
    """
    Esta funcion mediante restas sucesivas, obtiene el valor
    del cociente y resto de dos números enteros
    """
    cociente = 0
    resto = 0

    ## PROCESO
    # Cuando dividendo y divisor son negativos (- ; -)
    if signo(dividendo) < 0 and signo(divisor) < 0:
        dividendo = signo(dividendo) * dividendo
        divisor = signo(divisor) * divisor
        while dividendo >= divisor:
            dividendo = dividendo - divisor
            resto = dividendo
            cociente = cociente + 1

    # Cuando dividendo es positivo y divisor negativo (+ ; -)
    elif signo(dividendo) > 0 and signo(divisor) < 0:
        divisor = signo(divisor) * divisor
        while dividendo >= divisor:
            dividendo = dividendo - divisor
            resto = dividendo
            cociente = cociente + 1

    # Cuando dividendo es negativo y divisor positivo (- ; +)
    elif signo(dividendo) < 0 and signo(divisor) > 0:
        dividendo = signo(dividendo) * dividendo
        while dividendo >= divisor:
            dividendo = dividendo - divisor
            resto = dividendo
            cociente = cociente + 1

    # Cuando dividendo y divisor son positivos (+ ; +)
    elif signo(dividendo) > 0 and signo(divisor) > 0:
        while dividendo >= divisor:
            dividendo = dividendo - divisor
            resto = dividendo
            cociente = cociente + 1

    ## SALIDA
    return(resto,cociente)

def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    valor = int(input("ingrese dividendo: "))
    valor2 = int(input("ingrese divisor: "))
    resultado = division_lenta(valor,valor2)
    print(resultado)

if __name__ == "__main__":
    principal()
