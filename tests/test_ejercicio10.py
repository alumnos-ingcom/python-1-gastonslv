################
# Gaston Silvestre - @gastonslv
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Estos son los test correspondientes al archivo `ejercicio10.py` que esta en
`src`
"""
from src.ejercicio10 import es_palindromo

def test_es_palindromo():
    """
    Test ejercicio 10
    """
    palabra = "neuquen"
    assert isinstance(palabra, str), "La variable es una cadena"
    assert es_palindromo(palabra) == True, "Es verdadero que 'palabra' se escribe igual de derecha a izquirda y viceversa"