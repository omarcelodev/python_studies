import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def pause(msg = "Pressione ENTER para continuar."):
    input(msg)

def open_files():
    try:
        clear()
        with open("dados.txt", "r") as file:
            print(file.read())
        pause()

    except FileNotFoundError:
        print("Arquivo não encontrado!")
        pause()
    
    finally:
        print("Programa Encerrado...")
    
open_files()