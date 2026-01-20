#Combinação poderosa(*args + **kwargs)

def register(*args, **kwargs):
    print("Valores:", args)
    print("Configurações:", kwargs)

register(nome = "marcelo", idade = 20)