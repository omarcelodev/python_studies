
def log_execucao(func):
    def wrapper():
        print("Iniciando função.")
        resultado = func()
        print("Finalizando função")
        return resultado
    return wrapper


@log_execucao
def ola():
    print("Olá, Mundo!")

ola()