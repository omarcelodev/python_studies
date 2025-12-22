#Exemplo com input

try:
    idade = int(input("Digite sua idade: "))
    print(f"Você tem {idade} anos.")
    
except ValueError:
    print("Isso não é um número.")