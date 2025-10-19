import random

participantes = []

def menu():
    print("===SORTEADOR DE EQUIPES===")

    while True:
        nome = input("Digite o nome do participante: ").strip()
        participantes.append(nome)

        if len(participantes) >= 4:
            resposta = input("Deseja adicionar mais um participante?(s/n): ").lower()
            if resposta == 'n':
                break
    
    print(participantes)

    lista = participantes[:]
    random.shuffle(lista)

    for i in range(0, len(lista), 2):
        enumerador = i + 1
        if i + 1 < len(lista):
            dupla = (lista[i], lista[i + 1])
            print(f"{enumerador}° Dupla:",dupla)
        else:
            sobra = lista[i]
            print(sobra)

menu()
    
    