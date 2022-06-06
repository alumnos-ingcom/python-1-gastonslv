################
# Gaston Silvestre - @gastonslv
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
4. Suma lenta
"""

def suma_lenta(numero, otro_numero):
    """"
    Suma lenta entre dos números enteros
    """
    ## Entrada = dos numeros

    ## Proceso
    if otro_numero >= 0:
        while otro_numero != 0:
            otro_numero =  otro_numero - 1
            numero = numero + 1
    elif otro_numero < 0:
        while otro_numero != 0:
            otro_numero =  otro_numero + 1
            numero = numero -1

    ## Salida
    return numero

def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    valor = int(input("Ingrese un numero:"))
    valor2 = int(input("Ingrese otro numero:"))
    resultado = suma_lenta(valor,valor2)
    print(resultado)

if __name__ == "__main__":
    principal()
