def valores():
    lista = ['Matematicas', 'Arte', 'Historia', 'Fisica']
    try:
        lista.pop(4)
    except IndexError:
        lista.append('0')
        print(lista)
    else:
        print(lista)

valores()