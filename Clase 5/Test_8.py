"""Uso de libreria de fecha y tiempo"""
"""
Conversion de fechas
"""

import datetime

fecha_1 = datetime.datetime(2024, 4, 23)
fecha_2 = datetime.datetime(2024, 4, 20)

if fecha_1 == fecha_2:
    print('Nacieron el mismo día.')

elif fecha_1 > fecha_2:
    print('El niño 2 es mayor que el niño 1')

else:
    print('El niño 1 es mayor que el niño 2')