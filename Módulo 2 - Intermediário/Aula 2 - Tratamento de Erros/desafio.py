import os

def clear():
    os.system('cls' if os.name == 'nt' else "clear")

def pause(msg = "Digite ENTER para continar"):
    input(msg)

def verify_file_exist():
    try:
        with open("names.txt", "r") as file:
            file.read()
        return True

    except FileNotFoundError:
        if input("Esse Arquivo não existe. Deseja cria-lo?(s/n)").lower() == 's':
            with open("names.txt", "x") as file:
                file.write("=== CADASTRO DE NOMES: ===\n")
            print("Arquivo criado com sucesso!")

def verify_names(name):
    with open("names.txt", "r") as file:
        for line in file:
            if name == line.strip():
                return True
    return False

def register_names():

    verify_file_exist()

    if verify_file_exist() == True:
        while True:
            clear()
            print("=== CADASTRO DE NOMES ===\n")

            name = input("Digite o nome para cadastro: ").lower()
    
            if verify_names(name) == True:
                print("Esse nome já está cadastrado\n")
                pause()
                continue
                
            if name == "":
                print("O campo nome não pode estar vazio\n")
                pause()
                continue

            with open("names.txt", "a") as file:
                file.write(f"{name}\n")
                print(f"\n{name} adicionado(a) com sucesso")
            print("Salvando Arquivo...\n")

            pause()
            clear()

            print("=== CADASTRO DE NOMES ===\n")
            if input("Deseja adicionar mais um cadastro?(s/n): ") == 'n':
                break
        
register_names()