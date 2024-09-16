"""Uso de la librería JSONn para tratar tipo de datos JSON"""

import json
"""Uso de la librería JSON"""
json_data = '{"nombre": "Python", "tipo": "Backend", "paradigma": "POO"}'

"""Convirtiendo a un dato manejable para python"""

print(json_data)

json_to_python = json.loads(json_data)
print(json_to_python)
print(type(json_to_python))