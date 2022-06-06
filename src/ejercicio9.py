################
# Gaston Silvestre - @gastonslv
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
9. Factores Primos
"""

def factores_primos(numero):
    """
    Esta funcion devuelve una lista con los factores primos de un numero.
    """
    ## Entrada
    primos = []

    ## Proceso
    if numero > 0:
        for i in range(2, numero):
            while numero % i == 0:
                primos.append(i)
                numero = numero / i
    else:
        raise ValueError("El numero utilizado es negativo/neutro (0), ingrese uno positivo")
    ## Salida
    return primos

def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    valor = int(input("Ingrese un numero entero: "))
    resultado = factores_primos(valor)
    print(resultado)

if __name__ == "__main__":
    principal()
