# Jeito errado de abrir o arquivo

arquivo = open("dados.txt", "r")
conteudo = arquivo.read()
print(conteudo)

#Problema: O Arquivo vai ficar aberto na memória