import random

participantes = []

def menu():
    print("=== SORTEADOR DE EQUIPES ===")

    while True:
        nome = input("Digite o nome do participante: ").strip()
        participantes.append(nome)

        if len(participantes) >= 4:
           resposta = input("Deseja adicionar mais um participante?(s/n): ").lower()
           
           if resposta == 'n':
               break
    sorteio()
           

def sorteio():
    participantes_copia = participantes[:]
    random.shuffle(participantes_copia)

    for i in range(0, len(participantes_copia), 2):
        if i + 1 < len(participantes_copia):
            duplas = (participantes_copia[i], participantes_copia[i + 1])
            print("Duplas Escolhidas: \n", duplas)
        else:
            sobra = participantes_copia[i]
            print("Pessao Sobrando: ", sobra)

menu()
    
    