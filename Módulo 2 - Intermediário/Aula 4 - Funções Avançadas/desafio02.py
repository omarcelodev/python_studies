#Desafios de map

def desafio01():
    numeros = [1, 2, 3, 4, 5]

    numeros_formatados = list(map(lambda x: f"Valor: {x}", numeros))

    print(numeros_formatados)

def desafio02():
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    pares = list(filter(lambda x: x % 2 == 0, numeros))

    multiplication = list(map(lambda x: x * 10, pares))

    print(multiplication)

def desafio03():
    from itertools import count, islice
    
    numeros_formatados = list(map(lambda x: f"Valor: {x}", islice(count(1), 10)))

    print(numeros_formatados)

desafio03()
