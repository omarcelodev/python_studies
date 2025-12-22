import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def names():
    while True:
        clear()
        name = input("Digite seu nome: ").lower()
       
        with open("names.txt", "a") as file:
            file.write(f"{name}\n")
        
        if input("Deseja continuar? (s/n): ").lower() == 'n':
            break

names()