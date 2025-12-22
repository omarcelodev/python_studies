#Quando usar finally

try:
    file = open("dados.txt", "r")
    print("file.read()")
except FileNotFoundError:
    print("Erro ao abrir o arquivo.")
finally:
    print("Encerrando programa.")

"""
Muito usado para:
-Fechar conexões
-Logs
-Mensagens finais
"""

#Erro comum
try:
    file = open("dados.txt", "r")
    print("file.read()")
except FileNotFoundError:
    pass
"""
Isso engole o erro e o usuário não sabe oq aconteceu
"""