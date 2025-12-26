def ex01():
    numeros = [1, 2, 3, 4, 5]

    quadrado = map(lambda x: x ** 2, numeros)

    for n in quadrado:
        print(n)

def ex02():
    palavras = ["python", "go", "java", "javascript", "ruby"]  

    palavras_maiusculas  = list(map(lambda x: x.upper(), palavras))

    print(palavras_maiusculas)

def ex03():
    numeros_strings = ["1", "2", "3", "4"]

    numeros_inteiros = list(map(int, numeros_strings))

    print(numeros_inteiros)

ex03()