#Decorator com função que recebe argumento

# Wrapper precisar aceitar *args e **kwargs

def decorator(func):
    def wrapper(*args, **kwargs):
        print("Antes")
        resultado = func(*args, **kwargs)
        print("Depois")

        return resultado
    return wrapper

@decorator
def soma(a, b):
    return a + b

print(soma(2, 3))