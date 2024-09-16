"""Control o gestión de excepciones"""

'''
Requisitos
'''

def test(a = input('Escribe tu numerador: '), b = input('Escribe tu denominador: ')):
    try:
        a = float(a)
        b = float(b)
        resultado = a / b

    except ZeroDivisionError:
        print('No se puede dividir por 0')

    except ValueError:
        print('No puedes escribir un tipo string')

    else:
        print('Resultado:', resultado)

test()