#Tratamento de erros

"""
Python quebra quando algo inesperado acontece
-Arquivo não existente
-Usuário digita letra onde era número
-Divisão por zero
-Caminho errado
-Permissão Negada

try/except serve para tentar algo perigoso e lidar com o erro sem crash 
"""

#Exemplos:

#Programa Frágil
def prg1():
    with open('arqivo_inexistente.txt)', 'r') as file:
        print(file.read())

#O Arqivo não existe, logo o programa vai crashar ao tentar rodar

#Programa Resistene
def prg2():
    try:
        with open('arquivo_inexistente.txt', 'r') as file:
            print(file.read())
    except:
        print("Erro ao abrir o arqivo.")

prg2()