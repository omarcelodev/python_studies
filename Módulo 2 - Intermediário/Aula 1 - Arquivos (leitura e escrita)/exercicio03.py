def names():
    qntd_name = 0

    with open("names.txt", "r") as file:
        for name in file:
            qntd_name += 1
    print(f"Total de nomes cadastrados: {qntd_name}")

names()

