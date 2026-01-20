#Decorator com lógica real

#Medir tempo de execução

import time

def medir_tempo(func):
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fim = time.time()
        print(f"Tempo: {fim - inicio:.4f}s")
        return resultado
    return wrapper

@medir_tempo
def loop():
    for _ in range(10_000_000):
        pass

loop()
