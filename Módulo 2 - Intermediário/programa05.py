#Escrita em Arquivos:

#Criar ou sobrescrever
with open('dados2.txt', 'w') as arquivo:
    arquivo.write("Olá Mundo!\n")
    arquivo.write("Python é top\n")

"""
with open('dados2.txt', 'w') as arquivo:
    arquivo.write("Reescrevendo dados!\n")
    arquivo.write("Olá de novo mundo!\n")
"""

#Acrescentando conteúdo
with open("dados2.txt", "a") as arquivo:
    arquivo.write("Nova linha adicionada")