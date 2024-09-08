"""Usando las propiedades de cadenas o strings"""

"""Método de separación de strings: .split()"""

cadena = 'Python para la predicción de fraudes bancarios'

cadena_sin_espacios = cadena.split()

print('Cadena separada por espacios en blanco: {}'.format(cadena_sin_espacios))

for palabra in cadena_sin_espacios:
    print(palabra.upper())