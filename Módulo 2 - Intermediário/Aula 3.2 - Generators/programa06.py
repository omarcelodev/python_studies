# Exemplo prático com Yield

# Processar arquivo grande

#jeito ruim
with open("names.txt") as f:
    linhas = f.readlines()

#jeito profissional
def ler_linhas(caminho):
    with open(caminho) as f:
        for linha in f:
            yield linha.strip()
