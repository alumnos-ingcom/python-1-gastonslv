################
# Gaston Silvestre - @gastonslv
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Estos son los test correspondienets al archivo `ejercicio4.py` que estan en
`src`
"""
from src.ejercicio4 import suma_lenta

def test_suma_lenta_positivos():
    """
    Prueba con numeros positivos
    """
    numero = 10
    otro_numero = 50
    resultado = suma_lenta(numero,otro_numero)
    assert isinstance(resultado,int), "El resultado debe ser un numero entero"
    assert resultado > 0, "El resultado debe ser positivo"
    
def test_suma_lenta_negativos():
    """
    Prueba con numeros positivos
    """
    numero = 10
    otro_numero = -50
    resultado = suma_lenta(numero,otro_numero)
    assert isinstance(resultado,int), "El resultado debe ser un numero entero"
    assert resultado < 0, "El resultado debe ser negativo"
