import operacoes as op
import os

def clear():
    os.system('cls' if os.name == 'nt' else clear)

def main():
    while True:
        clear()
        n1 = int(input("Digite o primeiro numero: "))
        n2 = int(input("Digite o segundo numero: "))

        print(f"{n1} + {n2} = {op.soma(n1, n2)}")
        print(f"{n1} - {n2} = {op.subtracao(n1, n2)}")
        print(f"{n1} * {n2} = {op.multiplicacao(n1, n2)}")

        if input("Deseja realizar outro cálculo?(s/n): ").lower() == 'n':
            break

main()