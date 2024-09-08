"""Usando las propiedades de cadenas o strings"""

nombre = input('Ingresa tu nombre: ')
apellido = input('Ingresa tu apellido: ')

nombre_completo = nombre + " "+ apellido

print('El tamaño de tu nombre es: {}'.format(len(nombre_completo)))

print('El resultado final en mayùscula es: {}'.format(nombre_completo.upper()))

if len(nombre) > len(apellido):
    print('El tamaño de tu nombre es más grande que tu apellido')
elif len(nombre) < len(apellido):
    print('El tamaño de tu apellido es más grande que tu nombre')
else:
    print('Tu nombre y apellido tienen el mismo tamaño')