################
# Gaston Silvestre - @gastonslv
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Estos son los test correspondientes al archivo `ejercicio7.py` que esta en
`src`
"""

from src.ejercicio7 import sexadecimal_a_decimal, decimal_a_sexadecimal

def test_sexadecimal_a_decimal():
    """
    En esta funcion, vemos si 20 hs, 3' y 15'' son los segundos que esperamos
    """
    horas = 20
    minutos = 3
    segundos = 15
    resultado = sexadecimal_a_decimal(horas,minutos,segundos)
    assert resultado == 72195

def test_decimal_a_sexadecimal():
    """
    Probamos la funcion precisa, que tiene en cuenta cada segundo que ingresamos
    """
    segundos = 74789
    resultado = decimal_a_sexadecimal(segundos)
    assert resultado == (20, 46, 29), "20hs, 46min, 29seg"
