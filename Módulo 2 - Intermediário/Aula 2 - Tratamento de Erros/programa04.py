#Quando usar finally

try:
    file = open("dados.txt", "r")
    print("file.read()")
except FileNotFoundError:
    print("Erro ao abrir o arquivo.")
finally:
    print("Encerrando programa.")