################
# Gaston Silvestre - @usuario_github
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Estos son los tests correspondientes al ejercicio1.py
"""

from src.ejercicio1 import convertir_a_centigrados, convertir_a_fahrenheit

def test_convertir_a_fahrenheit_positivo():
    """
    Caso positivo de la funcion
    """
    numero = 30
    resultado = convertir_a_fahrenheit(numero)
    assert isinstance(resultado, float), "El resultado es un numero flotante"
    assert resultado > 0, "El resultado es positivo"
    assert resultado == 86.0, "El resultado esperado"

def test_convertir_a_fahrenheit_negativo():
    """
    Caso negativo de la funcion
    """
    numero = -30
    resultado = convertir_a_fahrenheit(numero)
    assert isinstance(resultado, float), "El resultado es un numero flotante"
    assert resultado < 0, "El resultado es positivo"
    assert resultado == -22.0, "El resultado esperado"

def test_convertir_a_centigrados_positivo():
    """
    Caso positivo de la funcion
    """
    numero = 50
    resultado = convertir_a_centigrados(numero)
    assert isinstance(resultado, float), "El resultado es un numero flotante"
    assert resultado > 0, "El resultado es positivo"
    assert resultado == 10.0, "El resultado esperado"

def test_convertir_a_centigrados_negativo():
    """
    Caso negativo de la funcion
    """
    numero = -50
    resultado = convertir_a_centigrados(numero)
    assert isinstance(resultado, float), "El resultado es un numero flotante"
    assert resultado < 0, "El resultado es positivo"
