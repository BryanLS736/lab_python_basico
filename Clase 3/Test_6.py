"""Listas en python"""

"""Listas count(): Cantidad de veces que aparece el elemento que se repite en una lista """

var_1 = ['python', 'java', 'PHP', 'JavaScript', 'typescript']

var_1.append('python')
var_1.append('python')
var_1.append('python')
var_1.append('NodeJS')

print('Mi lista actualizada tiene los siguientes valores: {}'.format(var_1))

print('La cantidad de veces que se repite la palabra "python" es: {}'.format(var_1.count('python')))