#Estrutura Completa

"""
try:
    # código que pode dar erro

except TipoDoErro:
    # o que fazer se der erro

else:
    # executa se não deu erro

finally:
    #executa sempre

"""

#Exemplo Claro

try:
    with open("names.txt", "r") as file:
        print(file.read())

except FileNotFoundError: #-> Erro específico é melhor que erro genérico
    print("Arquivo não encontrado.")

