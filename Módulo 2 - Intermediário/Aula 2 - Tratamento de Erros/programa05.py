#Aplicando Try/Except ao ultimo exercicio da Aula 1

def total_nomes():
    try:
        with open("names.txt", "r") as file:
            total = len(file.readlines())
        print(f"Total de nomes cadastrados: {total}")
    except FileNotFoundError:
        print("Arquivo de nomes não encontrado.")

total_nomes()