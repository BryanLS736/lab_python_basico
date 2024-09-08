"""
Programaciòn orientada a objetos
"""

"""Siempre inicia con mayuscula"""

class Carro:
    """Atributos"""
    ruedas = 4

    """Constructor: Valores que van a tener por defecto mi clase que se le instancia a una variable"""

    def __init__(self, color, aceleracion):
        self.color = color
        self.aceleracion = aceleracion
        self.velocidad = 0

    """Métodos: Son las funciones de las clases"""

    def acelerar(self):
        self.velocidad = self.velocidad - self.aceleracion


    def frenar(self):
        velocidad = self.velocidad - self.aceleracion
        if velocidad < 0:
            velocidad = 0

        self.velocidad = velocidad


"""Instanciamos nuestra clase"""

carro_1 = Carro('Negro', 60)
print(f'El color del primer carro es: {carro_1.color}')
print(f'La aceleracion de mi primer carro es: {carro_1.aceleracion}')
print(f'La cantidad de ruedas que tienen mi primer carro es: {carro_1.ruedas}')

carro_2 = Carro('Azul', 80)
print(f'El color del segundo carro es: {carro_2.color}')
print(f'La aceleracion de mi segundo carro es: {carro_2.aceleracion}')
print(f'La cantidad de ruedas que tienen mi segundo carro es: {carro_2.ruedas}')