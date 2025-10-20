import time
from datetime import datetime

def relogio():
    print("=== RÉLOGIO ===")
    while True:
        agora = datetime.now()
        horas = agora.hour
        minutos = agora.minute
        segundos = agora.second

        print(f"{horas:02d}:{minutos:02d}:{segundos:02d}", end='\r')
        time.sleep(1)

relogio()