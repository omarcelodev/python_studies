# *Args - Permite passar quantos argumentos quiser para uma função

#Exemplo simples

def soma(*args):
    return sum(args)

print(soma(1, 2, 3))
print(soma(10, 20, 30, 40))

#args vira uma tupla

