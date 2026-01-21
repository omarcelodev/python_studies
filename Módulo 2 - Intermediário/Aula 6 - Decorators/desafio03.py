def validar_int(func):
    def wrapper(*args, **kwargs):
        resultado = func(*args, **kwargs)
        if not isinstance(resultado, int):
            print("Retorno Inválido")
            return None
        return resultado
    return wrapper

@validar_int
def return_int():
    return 10

@validar_int
def return_string():
    return "Olá Mundo"

print(return_int())
print(return_string())