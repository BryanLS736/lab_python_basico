"""Control o gestión de excepciones"""

"""
TypeError
ZeroDivisionError
IndexError
KeyError
FileNotFoundError
ImportError
OverFlowError
"""

"""Estructura y uso"""

"""

Try:
    bloque código 1
except 'excepción 1'
    bloque código 2
else:
    bloque código 3

"""

def division(a, b):
    try:
        resultado = a/b
        print('Divisiòn correcta')
    except ZeroDivisionError:
        print('¡No es posible dividir entre cero estos valores!')
        resultado = None
        print(f'Resultado: {resultado}')
    else:
        print(f'Resultado: {resultado}')

division(1000,5)
division(400,0)
division(2, 500)