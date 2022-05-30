################
# Gaston Silvestre - @gastonslv
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
10. Palíndromo
"""
def es_palindromo(texto):
    """
    Esta funcion devuelve 'True' si la palabra ingresada
    se lee igual de derecha a izquierda que de izquierda a derecha.
    """

    ## Entrada
    texto_palindromo = ''

    ## Proceso
    for i in texto:
        texto_palindromo = i + texto_palindromo
    if texto_palindromo == texto:
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
    valor = str(input("Ingrese una palabra: "))
    resultado = es_palindromo(valor)
    print(resultado)

if __name__ == "__main__":
    principal()
