################
# Gaston Silvestre - @gastonslv
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
11. Multiplos de
"""
def es_multiplo(numero, multiplo):
    """
    Funcion que devuelve 'True' si numero es multiplo del segundo argumento que ingresemos.
    """
    ## Entrada
    contador = 0

    ## Proceso
    while contador != multiplo and contador < multiplo:
        contador = contador + numero
    if contador == multiplo:
        resultado = True
    else:
        resultado = False

    ## Salida
    return resultado

def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    valor = int(input("Ingrese un numero: "))
    valor2 = int(input("Ingrese el multiplo: "))
    resultado = es_multiplo(valor,valor2)
    print(resultado)

if __name__ == "__main__":
    principal()
