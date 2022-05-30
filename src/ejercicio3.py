################
# Gaston Silvestre - @gastonslv
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
3. Comparación de números
"""

def compara(numero, otro_numero):
    """
    Esta funcion acepta dos argumentos, los cuales son comparados
    y devuelve los resultados:
    * -1 si el primero es menor que el segundo
    *  0 si son iguales
    *  1 si el primero es mayor que el segundo
    """
    ## Entrada
    valor_numero = numero - otro_numero
    valor_otro_numero = otro_numero - numero

    ## Proceso
    if valor_numero < valor_otro_numero:
        resultado = -1
    elif valor_numero > valor_otro_numero:
        resultado = 1
    else:
        resultado = 0

    ## Salida
    return resultado

def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    valor = int(input("Ingrese un número: "))
    valor2 = int(input("Ingrese otro número: "))
    resultado = compara(valor,valor2)
    print(resultado)

if __name__ == "__main__":
    principal()
