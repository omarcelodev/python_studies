import os

def clear():
    os.system('cls' if os.name == 'nt' else clear)

def pause(msg = "Digite ENTER para continuar!"):
    input(msg)

def division():
    while True:
        clear()
        try:
            number_1 = float(input("Digite o primeiro número: "))
            number_2 = float(input("Digite o segundo número: "))
            result = number_1 / number_2
            print(f"{number_1} / {number_2} = {result:.2f}")

            pause()
            clear()

            if input("Deseja fazer uma nova divisão?(s/n): ").lower() == 's':
                continue

            break

        except ValueError:
            print("Número inválido!")
            pause()
        
        except ZeroDivisionError:
            print("ERRO. Divisão por zero é inválida")
            pause()

    print("Programa encerrado...")

division()