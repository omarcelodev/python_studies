def contar_chamadas(func):
    total = 0
    def wrapper(*args, **kwargs):
        nonlocal total
        total += 1
        print(f"funcão chamada {total} vezes")
        return func(*args, **kwargs)
    return wrapper

@contar_chamadas
def minha_funcao():
    print("Função executada")

minha_funcao()
minha_funcao()
minha_funcao()
minha_funcao()

