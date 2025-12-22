#Arquivos em CSV(Visão Geral)

with open("dados.csv", "r") as arquivo:
    for linha in arquivo:
        dados = linha.strip().split(",")
        print(dados)