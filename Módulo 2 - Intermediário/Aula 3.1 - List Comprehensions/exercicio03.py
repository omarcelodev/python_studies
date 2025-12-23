def main():
    try:
        with open('names.txt', 'r') as file:
            names = [line.strip() for line in file if len(line) > 4]
            print(names)
    except FileNotFoundError:
        print("Arquivo não encontrado!")

main()