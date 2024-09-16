"""Uso de libreria de fecha y tiempo"""
"""Basado en el sistema operativo"""

from datetime import datetime, date

str_date = "2/6/2024"

"""
d: dia
m: mes
y: año

"""

conversion = datetime.strptime(str_date, "%m/%d/%Y")
print(conversion)

"""Traer el mes de la fecha con formato en letras: strftime de datime"""

conversion_mes = datetime.strftime(conversion, '%d %b del %Y')
print(conversion_mes)

"""
b: reemplaza a "m" para mostrar el mes de forma literal
"""