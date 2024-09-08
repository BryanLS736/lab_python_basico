"""Programación funcional en python"""

num_1 = float(input('Ingresa tu primer numero: '))
num_2 = float(input('Ingresa tu segundo numero: '))
num_3 = float(input('Ingresa tu tercer numero: '))
num_4 = float(input('Ingresa tu cuarto numero: '))

def maximo(a, b, c, d):
    return max(a, b, c, d)

num_max = maximo(num_1, num_2, num_3, num_4)
cubo = pow(num_max, 3)
print(f'El cubo del numero mayor es: {cubo}')