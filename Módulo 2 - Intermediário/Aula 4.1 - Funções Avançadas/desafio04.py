#Desafios de Reduce

from functools import reduce

def desafio01():
    palavras = ["Python ", "é ", "bom"]

    frase = reduce(lambda a, b: a + b, palavras)

    print(frase)

def desafio02():
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    soma_pares = reduce(lambda a, b: a + b, filter(lambda x: x % 2 == 0, numeros))

    print(soma_pares)

def desafio03():
    produto_pares = reduce(lambda a, b: a * b, filter(lambda x: x % 2 == 0, range(1,11)))

    print(produto_pares)

desafio03()
