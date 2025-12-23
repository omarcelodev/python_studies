def filtrar_palavras(palavras):
    return (p.upper() for p in palavras if len(p) > 4)

for p in filtrar_palavras(["python", "c", "java", "go", "javascript"]):
    print(p)