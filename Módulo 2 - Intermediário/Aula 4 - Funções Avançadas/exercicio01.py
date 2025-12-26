def ex01():
    dobro = lambda x: x * 2
    number = int(input("Digite um número: "))
    print(dobro(number))

def ex02():
    string_upper = lambda x: x.upper()
    string = input("Digite alguma palavra: ")
    print(string_upper(string))

def ex03():
    maior = lambda x, y: x > y 

    number1 = int(input("Digite o primeiro número: "))
    number2 = int(input("Digite o segundo número: "))

    print(maior(number1, number2))
    
ex03()