#*Kwargs - Argumentos noemados dinâmicos
# Permite passar chave = valor sem saber quantos serão

#Exemplo

def usuario(**kwargs):
    for chave, valor in kwargs.items():
        print(f"{chave}:{valor}")

usuario(nome = "Marcelo", idade = 20, curso = "Engenharia de Software")

#Kwargs vira um dicionário