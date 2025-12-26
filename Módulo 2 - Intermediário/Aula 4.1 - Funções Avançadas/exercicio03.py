# Exercicios de filter

def ex01():
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    pares = list(filter(lambda x: x % 2 == 0, lista))

    print(pares)

def ex02():
    lista = ["python", "javascript", "java", "c", "go", "ruby"]

    palavras_filtradas = list(filter(lambda x: len(x) > 4, lista))

    print(palavras_filtradas)

def ex03():
    lista = ["python", "", "java", "", "go", ""]
    
    lista_filtrada = list(filter(None, lista))

    print(lista_filtrada)

ex03()