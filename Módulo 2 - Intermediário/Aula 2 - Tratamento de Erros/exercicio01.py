import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def pause(msg = "Digite ENTER para continuar"):
    input(msg)

def get_numbers():
    while True:
        clear()
        try:
            number = int(input("Digite um número inteiro: "))
            print(f"Você digitou o número: {number}")
            break
        except ValueError:
            print("Tipo inválido!")
            pause()

    print("Programa Encerrado!")

get_numbers()