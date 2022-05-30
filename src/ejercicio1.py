################
# Gaston - @gastonslv
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
1. Conversion de temperaturas
"""

def convertir_a_fahrenheit(centigrados):
    """
    Esta funcion convierte grados centigrados a fahrenheit
    """
    farenheit = (centigrados * 9/5) + 32
    return farenheit

def convertir_a_centigrados(fahrenheit):
    """
    Esta funcion convierte grados fahrenheit a centigrados
    """
    centigrados = (fahrenheit - 32) * (5/9)
    return centigrados

def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio1
    (La entrada, la llamada al algoritmo y la salida)
    """
    valor = float(input("Ingrese grados Celcius: "))
    resultado = convertir_a_fahrenheit(valor)
    print(f"La Temperatura {valor} C° es igual a {resultado} F°")
    valor2 = float(input("Ingrese grados Fahrenheit: "))
    resultado2 = convertir_a_centigrados(valor2)
    print(f"La Temperatura {valor2} F° es igual a {resultado2} C°")

if __name__ == "__main__":
    principal()
