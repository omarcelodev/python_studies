# Reduce - Reduz uma sequência ineira a um único valor -> ele acumula

#Sintaxe
def sintaxe():
    from functools import reduce

    reduce(function, iter)

#Exemplo
def exemplo():
    from functools import reduce

    numeros = [1, 2, 3, 4, 5]

    soma = reduce(lambda a, b: a + b, numeros)

    print(soma)

exemplo()