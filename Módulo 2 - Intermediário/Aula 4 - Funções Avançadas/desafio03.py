# Desafios de filter
def desafio01():
    numeros = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]

    numeros_positivos = list(filter(lambda x: x > 0, numeros))
    print(numeros_positivos)

def desafio02():
    from itertools import count, islice
    pares = list(filter(lambda x: x % 2 == 0, islice(count(1), 20)))

    print(pares)

def desafio03():
    from itertools import count, islice

    numeros_pares = list(map(lambda x: f"Valor: {x}",filter(lambda x: x % 2 == 0, islice(count(1), 30))))

    print(numeros_pares)

desafio03()