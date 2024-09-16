def impuesto():
    sueldo = float(input('Ingrese el sueldo: '))
    if sueldo > 500:
        print('Usted tiene que pagar un impuesto del 8%.')
        imp = sueldo * 0.08
        print(f'El impuesto a pagar es de {imp}')
    else:
        print('Usted no debe de pagar ningun impuesto.')