import requests
import random
import time
from datetime import datetime

API_URL = "http://localhost:8000/data"

# Valores realistas para Bogotá en la noche
temperatura = 13.5
humedad = 82.0
presion = 752.0

while True:
    temperatura += random.uniform(-0.2, 0.2)
    humedad += random.uniform(-1.0, 1.0)
    presion += random.uniform(-0.5, 0.5)

    temperatura = round(max(8, min(18, temperatura)), 2)
    humedad = round(max(65, min(98, humedad)), 2)
    presion = round(max(740, min(765, presion)), 2)

    datos = {
        "temperatura": temperatura,
        "humedad": humedad,
        "presion": presion
    }

    try:
        respuesta = requests.post(API_URL, json=datos)
        print(datetime.now(), datos, respuesta.status_code)
    except Exception as e:
        print("Error enviando datos:", e)

    time.sleep(5)