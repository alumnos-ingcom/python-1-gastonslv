################
# Gaston Silvestre - @gastonslv
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Estos son los test correspondientes al archivo `ejercicio6.py` que esta en
`src`
"""

from src.ejercicio6 import ordenar_mayor_a_menor, ordenar_menor_a_mayor

def test_mayor_a_menor():
    """
    Test de la funcion con numeros positivos y negativos
    """
    numero = -1
    numero_dos = 2
    numero_tres = 3
    resultado = ordenar_mayor_a_menor(numero,numero_dos,numero_tres)
    assert resultado == (3,2,-1), "El resultado esperado"

def test_menor_a_mayor():
    """
    Test de la funcion con numeros positivos y negativos
    """
    numero = -1
    numero_dos = 2
    numero_tres = 3
    resultado = ordenar_menor_a_mayor(numero,numero_dos,numero_tres)
    assert resultado == (-1,2,3), "El resultado esperado"
