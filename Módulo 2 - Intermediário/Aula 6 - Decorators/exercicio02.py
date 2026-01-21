def dobrar_retorno(func):
    def wrapper():
        resultado = func()

        return resultado * 2
    
    return wrapper

@dobrar_retorno
def numero():
    return 10

print(numero())