#Leitura de Arquivos
import time

#Lê todo o arquivo
with open('dados.txt', "r") as arquivo:
    print(arquivo.read())

#Lê linha por linha
with open('dados.txt') as arquivo:
    for linha in arquivo:
        print(linha.strip())
        time.sleep(1)
        

#strip() remove a quebra de linha \n
