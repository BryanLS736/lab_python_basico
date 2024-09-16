"""Uso de libreria de fecha y tiempo"""
"""
Conversion total del tiempo
"""

from datetime import datetime

"""Uso del método: timestamp"""

time_now = datetime.strptime('2024/05/02 20:30:00', '%Y/%m/%d %H:%M:%S').timestamp()

print(time_now)