################
# Gaston Silvestre - @gastonslv
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Enunciado del ejercicio
"""
def sexadecimal_a_decimal(horas, minutos, segundos):
    """
    Esta función convierte las horas, minutos y segundos a segundos.
    """
    ## Proceso
    horas = (horas * 60) * 60
    minutos = minutos * 60
    resultado = horas + minutos + segundos

    ## Salida
    return resultado

def decimal_a_sexadecimal(numero):
    """
    Esta funcion convierte segundos a (horas,minutos,segundos).
    """
    ## Entrada
    horas = 0
    minutos = 0
    contador_segundos = 0
    residuo = 0

    ## Proceso
    while numero != 0:
        numero = numero - 1
        residuo = residuo + 1
        if residuo == 3600:
            horas += 1
            residuo = 0

    if residuo >= 60:
        while residuo != 0:
            residuo = residuo - 1
            contador_segundos += 1
            if contador_segundos == 60:
                minutos += 1
                contador_segundos = 0
    else:
        contador_segundos = residuo

    numero = (horas,minutos,contador_segundos)

    ## Salida
    return numero

def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    valor = int(input("ingrese segundos: "))
    resultado = decimal_a_sexadecimal(valor)
    print(resultado)
    valor_hs = int(input("ingrese horas: "))
    valor_min = int(input("ingrese minutos: "))
    valor_s = int(input("ingrese segundos: "))
    resultado2 = sexadecimal_a_decimal(valor_hs, valor_min, valor_s)
    print(f"{resultado2} segundos")

if __name__ == "__main__":
    principal()
