"""Uso de bucle while"""

numero = int(input('¿Cúantos saludos desea enviar?: '))

while numero < 10:
    print(numero)
    numero = numero+1
    # El número ya aumentó un valor
    print('Número con nuevo valor: {}'.format(numero))