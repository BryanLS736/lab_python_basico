"""Escribimos nuestras variables"""

nombre = input('Ingresa tu nombre: ')
apellido = input('Ingresa tu apellido: ')
distrito = input('Ingresa tu distrito: ')
sueldo = input('Ingresa tu sueldo: ')

"""Calculamos el bono final"""

bono_final = (3*int(sueldo))-0.1*int(sueldo)

"""Creamos nuestro diccionario"""

diccionario = {'nombre': nombre, 'apellido': apellido, 'distrito': distrito, 'sueldo': sueldo, 'bono_final': bono_final}

"""Creamos nuestras 3 variables para los valores del diccionario"""

nombre_diccionario = diccionario['nombre']
apellido_diccionario = diccionario['apellido']
bono_final_diccionario = diccionario['bono_final']

"""Imprimimos en pantalla el mensaje final"""

print('{} {}, recibirá {} soles de bono de fin de año'.format(nombre, apellido_diccionario, bono_final_diccionario))
