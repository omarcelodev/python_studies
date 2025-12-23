# List Comprehensions -> É uma forma curta, clara e eficiente de criarr listas a partir de outra sequência
# Ela substitui loops + append

def jeito_tradicional():
    numeros = [1, 2, 3, 4, 5]
    quadrados = []

    for n in numeros:
        quadrados.append(n ** 2)
        
    print(quadrados)

jeito_tradicional()


def jeito_pythonic():
    numeros = [1, 2, 3, 4, 5]
    quadrados = [n ** 2 for n in numeros]

    print(quadrados)

jeito_pythonic()

"""
Mesma coisa
Menos linhas
Mais legível para quem sabe Python
"""