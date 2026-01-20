#Decorator com lógica real

#Decorator de permissão

def requer_login(func):
    def wrapper(usuario):
        if usuario != "admin":
            print("Acesso negado")
            return
        return func(usuario)
    return wrapper

@requer_login
def painel(usuario):
    print("Bem-Vindo ao painel")

painel("admin")
painel("guest")