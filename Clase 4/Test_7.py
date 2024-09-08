"""Uso del condicional 'if'"""
"""if ternarios"""

"""
Requisitos:
    -Ingresar por teclado el sueldo 
    - Ingresar por teclado el sueldo de un empleado
    - Si el sueldo es mayor a 3500, imprimir "Su sueldo no tiene bonificación"
    - Caso contrario: "Su sueldo tiene bonificación este año y será de: sueldo_final", sueldo_final= sueldo + 20% sueldo
"""

sueldo = float(input('Ingresa el sueldo: '))

if sueldo > 3500.0:
    print('Su sueldo no tiene bonificación')
else:
    sueldo_final = sueldo + (0.2 * sueldo)
    print('Su sueldo tiene bonificación este año y será de: {}'.format(sueldo_final))