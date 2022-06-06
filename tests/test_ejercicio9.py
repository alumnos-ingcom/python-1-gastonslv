################
# Gaston Silvestre - @gastonslv
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Estos son los test correspondientes al archivo `ejercicio9.py` que esta en
`src`
"""

from src.ejercicio9 import factores_primos

def test_nombrefuncion():
    """
    Test del ejercicio 9
    """
    numero = 85
    assert factores_primos(numero) == [5,17], "Resultado esperado"
