with open("mensagem.txt", "w") as file:
    file.write("Aprender Pyhon é um processso.\n")
    file.write("Constância vence talento.\n")

with open("mensagem.txt", "r") as file:
    print(file.read())