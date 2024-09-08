"""
Programación oriendada a objetos
Participación
"""

class Alumno:
    nacionalidad = 'Peruano'

    def __init__(self, nombre, distrito, nota_1=0, nota_2=0, nota_3=0):
        self.nombre = nombre
        self.distrito = distrito
        self.nota_1 = nota_1
        self.nota_2 = nota_2
        self.nota_3 = nota_3
        self.aprobado = False
        self.prom = 0


    def promedio(self):
        self.prom = (self.nota_1 + self.nota_2 + self.nota_3)/3


    def aprob(self):
        promedi = self.prom
        if promedi >= 11:
            self.aprobado = 'Aprobado'
        else:
            self.aprobado = 'Desaprobado'



alumno_1 = Alumno('Bryan', 'Ate',18,14,11)

alumno_1.promedio()
alumno_1.aprob()
print(f'El nombre del primer alumno es: {alumno_1.nombre}, y pertenece al distrito de: {alumno_1.distrito}')
print(f'Obtuvo un promedio de: {alumno_1.prom}')
print(f'Su estado es: {alumno_1.aprobado}')

print()

alumno_2 = Alumno('Alexander', 'Lima',4, 20, 4)

alumno_2.promedio()
alumno_2.aprob()

print(f'El nombre del segundo alumno es: {alumno_2.nombre}, y pertenece al distrito de: {alumno_2.distrito}')
print(f'Obtuvo un promedio de: {alumno_2.prom}')
print(f'Su estado es: {alumno_2.aprobado}')