# A mágica do @

def meu_decorator(func):
    def wrapper():
        print("Antes da função")
        func()
        print("Depos da função")
    return wrapper

#Isso aqui:
@meu_decorator
def diga_oi():
    print("Oi")

#É igual a isso
""""
diga_oi = meu_decorator(diga_oi)
"""

diga_oi()


