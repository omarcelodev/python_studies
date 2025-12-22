#Jeito Certo de Abrir o Arquivo

with open("dados.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)