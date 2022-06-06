################
# Gaston Silvestre - @gastonslv
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Estos son los test correspondienets al archivo `ejercicio3.py` que estan en
`src`
"""
from src.ejercicio3 import compara

def test_comprara_positivo():
    """
    Caso positivo de la funcion
    """
    numero = 10
    numero_dos = 30
    resultado = compara(numero,numero_dos)
    assert isinstance(resultado,int), "El resultado debe ser un numero entero"
    assert resultado == -1 ,"-1 si el primero es menor que el segundo"
    assert resultado < 0, "el resultado debe ser negativo"

def test_compara_negtivo():
    """
    Caso negativo
    """
    numero = 20
    numero_dos = -15
    resultado = compara(numero,numero_dos)
    assert isinstance(resultado,int), "El resultado debe ser un numero entero"
    assert resultado == 1 ,"1 si el primero es mayor que el segundo"
    assert resultado > 0, "el resultado debe ser un numero positivo"

def test_compara_cero():
    """
    Caso cero
    """
    numero = 0
    numero_dos = 0
    resultado = compara(numero,numero_dos)
    assert isinstance(resultado,int), "El resultado debe ser un numero entero"
    assert resultado == 0 ,"0 si son iguales"
    assert resultado == 0, "el resultado debe ser cero"
  