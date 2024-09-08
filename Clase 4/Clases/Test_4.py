"""
Programaciòn orientada a objetos
"""

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
        self.velocidad = self.velocidad + self.aceleracion


    def frenar(self):
        velocidad = self.velocidad - self.aceleracion
        if velocidad < 0:
            velocidad = 0

        self.velocidad = velocidad


"""Aplicamos herencia"""
"""Creamos nuestra clase hija"""

class CarroVolador(Carro):
    ruedas = 6

    def __init__(self, color, aceleracion, estado_volando = False):
        """El super nos indica la herencia"""
        super().__init__(color, aceleracion)
        self.color = color
        self.aceleracion = aceleracion
        self.estado_volando = estado_volando


    def vuela(self):
        self.estado_volando = True


    def aterriza(self):
        self.estado_volando = False


carro_1 = Carro('Rojo', 55)

carro_volador = CarroVolador('Azul', 65)

print(f'El color de carro volador es: {carro_volador.color}')
print(f'El estado de mi velocidad de mi carro volador es: {carro_volador.aceleracion}')

carro_volador.vuela()
carro_volador.acelerar()
carro_volador.acelerar()
carro_volador.acelerar()

print(f'La velocidad actual de mi carro volador es: {carro_volador.velocidad}')

"""Esto no puede suceder, porque la herencia es sólo de la clase hija"""
# carro_1.vuela()