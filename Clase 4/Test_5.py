"""Uso de 'for'"""

ingenierias = ['Software', 'Sistemas', 'Industrial', 'Quimica', 'Mecanica', 'Mecatronica']

print('El temaño de la lista es de: {}'.format(len(ingenierias)))

i = 0

for ingenieria in ingenierias:
    print(ingenieria)
    i = i + 1
    print('Valor de i: {}'.format(i))