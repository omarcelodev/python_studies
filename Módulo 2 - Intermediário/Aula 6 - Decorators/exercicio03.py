def verificar_zero(func):
    def wrapper(*args):
        if 0 in args:
            print("Erro: zero não permitido")
            return 
        return func(*args)
    return wrapper

@verificar_zero
def dividir(a, b):
    return a / b

print(dividir(0, 10))
print(dividir(20, 10))