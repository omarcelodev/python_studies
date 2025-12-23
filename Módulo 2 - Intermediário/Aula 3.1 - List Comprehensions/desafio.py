def main():
    palavras = ["python", "java", "c", "javascript", 'go']
    new_palavras = [palavra.upper() for palavra in palavras if len(palavra) > 3]
    print(new_palavras)

main()