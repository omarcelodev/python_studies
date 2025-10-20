#Gerenciador de Inventário de RPG
inventario = [
    {"nome": "Poção de Vida", "tipo": "poção", "quantidade": 3},
    {"nome": "Poção de Mana", "tipo": "poção", "quantidade": 2},
    {"nome": "Espada Longa", "tipo": "arma", "quantidade": 1},
    {"nome": "Escudo de Ferro", "tipo": "equipamento", "quantidade": 1},
    {"nome": "Moeda de Ouro", "tipo": "miscelânea", "quantidade": 50}
]

def menu():
    while True:
        print("=== INVENTARIO ===")
        print("(1) Adicionar Item")
        print("(2) Remover Item ")
        print("(3) Consultar Item")
        print("(4) Ver resumo do Inventário")
        print("(5) Salvar Inventário")
        print("(0) Sair do Inventário")
        opcao = int(input("Sua opção: "))

        if opcao == 1:
            print("Função")
        elif opcao == 2:
            print("Função")
        elif opcao == 3:
            print("Função")
        elif opcao == 4:
            print("Função")
        elif opcao == 5:
            print("Função")
        elif opcao == 0:
            break
        else:
            print("Opção Inválidada! Tente Novamente.")

menu()