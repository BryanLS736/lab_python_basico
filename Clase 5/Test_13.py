"""
    Decoradores en Python
"""

"""Creación interna de la función decoradora"""

def funcionADecoradora(funcionB):


    def funcionC(*args, **kwargs):
        print('1. Antes de ejecutar la función a decorar')
        resultado = funcionB(*args, **kwargs)
        print('2. Después de ejecutar la función a decorar')
        return resultado
    return funcionC


@funcionADecoradora
def saludar(nombre, apellido, edad, **kwargs):
    print(f'Hola {nombre} {apellido}, usted tiene {edad} años.')
    for key, value in kwargs.items():
        print(f"{key} = {value}")



saludar('Julio', 'Gutierrez', 29, ciudad1 = 'Lima', ciudad2 ='Tacna', ciudad3 = 'Arequipa')
