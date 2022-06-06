################
# Gaston Silvestre - @gastonslv
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Estos son los tests correspondientes al ejercicio2.py
"""
from src.ejercicio2 import signo

def test_signo_pos():
    """
    Testeamos la parte positiva de la funcion
    """
    numero = 10
    resultado = signo(numero)
    assert isinstance(numero,int), "El numero es un entero"
    assert resultado > 0, "El resultado tiene que ser positivo"
    assert resultado == 1, "El resultado es igual a '1'"

def test_signo_neutro():
    """
    Testeamos la parte neutra de la funcion
    """
    numero = 0
    resultado = signo(numero)
    assert isinstance(numero,int), "El numero es un entero"
    assert resultado == 0, "El resultado es neutro"

def test_signo_neg():
    """
    Testeamos la parte negativa de la funcion
    """
    numero = -31
    resultado = signo(numero)
    assert isinstance(numero,int), "El numero es un entero"
    assert resultado < 0, "El resultado es negativo"
    assert resultado == -1, "El resultado tiene que ser '-1'"
