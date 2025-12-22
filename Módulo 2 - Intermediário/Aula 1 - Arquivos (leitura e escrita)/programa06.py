#Arquivos em CSV(Visão Geral)

with open("dados.csv", "r") as arquivo:
    for linha in arquivo:
        dados = linha.strip().split(",")
        print(dados)

"""
Erros comuns:

- Esquecer o `with`
- Usar `'w'` achando que vai só escrever uma linha
- Não tratar arquivo inexistente (vamos resolver isso no próximo tópico)
"""