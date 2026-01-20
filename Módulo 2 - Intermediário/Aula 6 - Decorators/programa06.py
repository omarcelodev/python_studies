#Decorator com lógica real

#Decorator com parâmetros

# Aqui tem 3 funções

def repetir(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repetir(3)
def falar():
    print("Olá")

falar()

