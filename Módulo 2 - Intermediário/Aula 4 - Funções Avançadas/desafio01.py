def desafio01():
    palavras =["python", "c", "java", "javascript", "go"]
    ordenadas = sorted(palavras, key= lambda x: len(x))

    print(ordenadas)

def desafio02():
    numeros = [-2, 9, 7, -3, -10, 10, 100, -6]
    negativos = filter(lambda x: x < 0, numeros)

    print(list(negativos))

def desafio03():
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    formatados = map(lambda x: f"Valor: {x}", numeros)

    print(list(formatados))

desafio02()