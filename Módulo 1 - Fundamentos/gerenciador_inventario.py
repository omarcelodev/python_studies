#Gerenciador de Inventário de RPG
itens = {
    "armas": [
        "espada longa",
        "espada curta",
        "adaga",
        "machado de batalha",
        "machado leve",
        "lança",
        "arco curto",
        "arco longo",
        "besta",
        "cajado magico",
        "martelo de guerra",
        "maça pesada",
        "foice",
        "chicote",
        "bastão de combate"
    ],

    "armaduras": [
        "armadura leve",
        "armadura media",
        "armadura pesada",
        "armadura de couro",
        "armadura de ferro",
        "armadura de aço",
        "armadura encantada",
        "malha",
        "escudo pequeno",
        "escudo grande"
    ],

    "pocoes_consumiveis": [
        "poçao de cura",
        "poçao de mana",
        "poçao de stamina",
        "poçao de força",
        "poçao de velocidade",
        "poçao de invisibilidade",
        "poçao de resistencia a dano",
        "comida simples",
        "refeiçao completa",
        "agua",
        "elixir raro"
    ],

    "itens_magicos": [
        "amuleto magico",
        "anel magico",
        "pergaminho de magia",
        "grimorio",
        "pedra elemental",
        "orbe arcano",
        "runa encantada"
    ],

    "materiais": [
        "madeira",
        "pedra",
        "minerio de ferro",
        "minerio de prata",
        "minerio de ouro",
        "couro",
        "tecido",
        "ossos",
        "cristais",
        "polvora"
    ],

    "utilidades": [
        "corda",
        "tocha",
        "kit de primeiros socorros",
        "chave misteriosa",
        "mapa antigo",
        "moedas de bronze",
        "moedas de prata",
        "moedas de ouro",
        "ferramentas",
        "livro antigo",
        "reliquia desconhecida"
    ],

    "itens_raros": [
        "espada lendaria",
        "armadura divina",
        "coroa ancestral",
        "pedra filosofal",
        "amuleto do tempo",
        "escudo indestrutivel",
        "arco celestial"
    ]
}

inventario = [
    {"nome": "poçao de cura", "tipo": "pocoes_consumiveis", "quantidade": 3},
    {"nome": "poçao de mana", "tipo": "pocoes_consumiveis", "quantidade": 2},
    {"nome": "espada longa", "tipo": "arma", "quantidade": 1},
    {"nome": "malha", "tipo": "armadura", "quantidade": 1},
    {"nome": "moedas de ouro", "tipo": "utilidades", "quantidade": 50},
]

#Adiciona a categoria do item automaticamente e verifica se o item está na lista de itens do jogo
def category_itens(name_item):
    for categoria, lista in itens.items():
        if name_item in lista:
            return categoria
                
    print("Esse item não existe no jogo.\n")
    return None

#Checa quanto do item já existe no inventário
def check_qntd_atual(name_item):
    for item in inventario:
        if item["nome"].lower() == name_item:
            return item["quantidade"]
    return 0

#Captura a quantidade de itens
def qntd_itens(name_item):
    MAX = 50

    while True:
        qntd_item = int(input("Digite a quantidade do item que deseja adicionar: "))
        qntd_atual = check_qntd_atual(name_item)

        if qntd_atual >= MAX:
            print(f"Seu inventário já atingiu o máximo de 50 {name_item}.\n")
            return 0
        
        if qntd_item < 1:
            print("Quantidade inválida!\n")
            continue
        
        free_space = MAX - qntd_atual

        if qntd_item > free_space:
            print(f"Só há espaço para {free_space} {name_item}.")
            print(f"Foram adicionado(s) {free_space} {name_item}.")
            return free_space
        
        return qntd_item
    
#Adiciona Itens no inventário
def add_item():
    print("\n===ADIÇÃO DE ITENS===")

    while True:
        name_item = input("Digite o nome do item que deseja adicionar: "
                          "Digite 0 para voltar ao menu").strip().lower()
        if category_itens(name_item) != None:
            break
    
    #Adiciona quantidade de um item já existente
    for item in inventario:
        if item["nome"].lower() == name_item:
            print("\nEsse item já está no seu iventário.")
            
            qntd_item = qntd_itens(name_item)
            item["quantidade"] += qntd_item

            if qntd_item != 0:
                print(f"Quantidade atualizada! Você tem {item['quantidade']} {item['nome']}.\n")
            return

    
    #Categoriza o item automaticamente. 
    type_item = category_itens(name_item)
    if type_item is None:
        return
        
    #Adiciona a quantidade de itens desejada
    qntd_item = qntd_itens(name_item)

    #Adiciona o novo item ao inventário
    new_item = {
        "nome": name_item, 
        "tipo": type_item, 
        "quantidade": qntd_item
    }

    inventario.append(new_item)

    print(inventario)
    
#Menu de Interação
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
            add_item()
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