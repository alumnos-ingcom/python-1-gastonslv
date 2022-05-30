################
# Gaston - @gastonslv
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
2. Números positivos y negativos
"""

def signo(numero):
    """
    Esta funcion especifica el tipo de signo que se ingresa
    """
    valor = numero + numero
    if valor > numero:
        signoh = 1
    elif valor == numero:
        signoh = 0
    else:
        signoh = -1
    return signoh

def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva'
    del ejercicio (La entrada, la llamada al algoritmo y la salida)
    """
    valor = int(input("Ingrese un número: "))
    resultado = signo(valor)
    print(resultado)

if __name__ == "__main__":
    principal()
