################
# Gaston Silvestre - @gastonslv
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
6. Ordenar 3 valores
"""

def ordenar_mayor_a_menor(uno, dos, tres):
    """
    A partir de tres variables de tipo entero retorna dichos
    valores ordenados de mayor a menor.
    """
    ## Entrada
    secuencia = (uno,dos,tres)

    ## Proceso
    if secuencia[0] > secuencia[1] and secuencia[0] > secuencia[2]:
        secuencia = (uno,dos,tres)
        if secuencia[1] > secuencia[2]:
            secuencia = (uno,dos,tres)
        else:
            secuencia = (uno,tres,dos)

    elif secuencia[1] > secuencia[0] and secuencia[1] > secuencia[2]:
        secuencia = (dos,uno,tres)
        if secuencia[1] > secuencia[2]:
            secuencia = (dos,uno,tres)
        else:
            secuencia = (dos,tres,uno)

    elif secuencia[2] > secuencia[0] and secuencia[2] > secuencia[1]:
        secuencia = (tres,uno,dos)
        if secuencia[1] > secuencia[2]:
            secuencia = (tres,uno,dos)
        else:
            secuencia = (tres,dos,uno)

    ## Salida
    return secuencia

def ordenar_menor_a_mayor(uno, dos, tres):
    """
    A partir de tres variables de tipo entero retorna dichos
    valores ordenados de menor a mayor
    """
    ## Entrada
    secuencia = (uno,dos,tres)

    ## Proceso
    if secuencia[0] > secuencia[1] and secuencia[0] > secuencia[2]:
        secuencia = (tres,dos,uno)
        if secuencia[0] > secuencia[1]:
            secuencia = (dos,tres,uno)
        else:
            secuencia = (tres,dos,uno)

    elif secuencia[1] > secuencia[0] and secuencia[1] > secuencia[2]:
        secuencia = (tres,uno,dos)
        if secuencia[0] > secuencia[1]:
            secuencia = (uno,tres,dos)
        else:
            secuencia = (tres,uno,dos)

    elif secuencia[2] > secuencia[0] and secuencia[2] > secuencia[1]:
        secuencia = (uno,dos,tres)
        if secuencia[0] > secuencia[1]:
            secuencia = (dos,uno,tres)
        else:
            secuencia = (uno,dos,tres)

    ## Salida
    return secuencia

def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    valor_uno = int(input("Ingrese un numero: "))
    valor_dos = int(input("Ingrese otro numero: "))
    valor_tres = int(input("Ingrese un último numero: "))
    resultado = ordenar_mayor_a_menor(valor_uno,valor_dos,valor_tres)
    print(f"{resultado} numeros ordenados de Mayor(>) a Menor(<).")
    resultado2 = ordenar_menor_a_mayor(valor_uno,valor_dos,valor_tres)
    print(f"{resultado2} numeros ordenados de menor(<) a mayor(>).")

if __name__ == "__main__":
    principal()
