#Decorator é uma função que
# - Recebe outra função
# - Adiciona comportamento
# - Devolve uma nova função, sem você mexer no código original

# Decorator é uma função especializada 

# Já fizemos isso

def potencia(exp):
    def calcular(x):
        return x ** exp
    return calcular

# Agora pensamos assim: E se em vez de x, eu recebesse uma função inteira?

#Decorator na forma bruta(sem @)

#Exemplo 1 - Decorator Simples

def meu_decorator(func):
    def wrapper():
        print("Antes da função")
        func()
        print("Depos da função")
    return wrapper
 
def diga_oi():
    print("Oi")

diga_oi = meu_decorator(diga_oi)

diga_oi()