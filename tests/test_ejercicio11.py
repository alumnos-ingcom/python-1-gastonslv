################
# Gaston Silvestre - @gastonslv
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Estos son los test correspondientes al archivo `ejercicio11.py` que esta en
`src`
"""

from src.ejercicio11 import es_multiplo

def test_es_multiplo_false():
    """
    Test ejercicio 11
    """
    numero = 10
    multiplo = 21
    assert es_multiplo(numero,multiplo) == False, "El resultado es falso"

def test_es_multiplo_true():
    """
    Test ejercicio 11
    """
    numero = 10
    multiplo = 100
    assert es_multiplo(numero,multiplo) == True, "El resultado es verdadero"
