"""Porgramación funcional con python"""
"""Separara tareas por funciones"""

var_1 = 80
var_2 = 180

"""Input: dos variables que pasarán por parámetros de la función"""
"""a,b: parámetros de la función 'sumar'"""


def sumar(a,b):
    return a + b

"""
def sumar(a,b):
    suma = a+b
    pot = 
    return suma
"""

resultado = sumar(var_1,var_2)

"""Output: lo que retorna la función"""

print(f'El resultado de la suma es: {resultado}')

resultado_2 = sumar(90.7, 150.70)
print(f'El resultado de la suma es: {resultado_2}')