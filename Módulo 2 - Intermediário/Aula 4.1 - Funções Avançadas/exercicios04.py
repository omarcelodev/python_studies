# Exercicios de Reduce
from functools import reduce

def ex01():
    numeros = [1, 2, 3, 4, 5]
    soma = reduce(lambda a, b: a + b, numeros)

    print(soma)

def ex02():
    numeros = [1, 2, 3, 4]
    multiplicacao = reduce(lambda a, b: a * b, numeros)

    print(multiplicacao)

def ex03():
    numeros = [3 , 7 , 2 , 9 , 5]

    maior_numero = reduce(lambda a, b: a if a > b else b, numeros)
    print(maior_numero)

ex03()