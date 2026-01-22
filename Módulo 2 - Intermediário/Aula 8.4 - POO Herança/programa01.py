# Herança
# - Criar uma classe nova baseada em outra classe

# A classe filha herda atributos e metodos da classe mãe

# Exemplo:

class Personagem:
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida
    
    def atacar(self):
        return f"{self.nome} atacou!"

class Guerreiro(Personagem):
    pass

# Mesmo sem escrever nada o guerreito já herda tudo da classe Personagem

g = Guerreiro("Thor", 100)

print(g.nome)
print(g.atacar())

