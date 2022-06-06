################
# Gaston Silvestre - @gastonslv
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
8. Números primos
"""
from ejercicio2 import signo

def es_primo(numero):
    """
    Esta funcion devuelve 'True' si el numero que se ingreso es primo,
    y 'False' en el caso contrario.
    """
    ## ENTRADA
    numero_modif = 0

    ## PROCESO
    # esta parte se cumple, si `numero` es positivo
    if signo(numero) == 1 or signo(numero) == 0:
        numero = numero % 2
        if numero == 1:
            resultado = True
        else:
            resultado = False

    # esta parte se cumple, si `numero` es negativo
    if signo(numero) == -1:
        numero_modif = numero * signo(numero)
        numero_modif = numero_modif % 2
        if numero_modif == 1:
            resultado = True
        else:
            resultado = False

    ## SALIDA
    return resultado

def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    valor = int(input("Ingrese un numero: "))
    resultado = es_primo(valor)
    print(resultado)

if __name__ == "__main__":
    principal()
