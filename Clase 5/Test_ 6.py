"""Uso de libreria de fecha y tiempo"""
"""Basado en el sistema operativo"""

from datetime import datetime, date

fecha = date.today()
print(fecha)

tiempo = datetime.now()
print(tiempo)

anio = tiempo.year
mes = tiempo.month
dia = tiempo.day

print(f'El año actual es: {anio}, mes: {mes}, dia: {dia}')

"""Uso de datetime para extraer la hora, el minuto y el segundo actual"""

hora = tiempo.hour
minuto = tiempo.minute
segundo = tiempo.second

print(F'Son las {hora} horas con {minuto} minutos y {segundo} segundos')