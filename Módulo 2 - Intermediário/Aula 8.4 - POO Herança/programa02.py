# Classe filha adicionando comportamento

class Personagem:
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida
    
    def atacar(self):
        return f"{self.nome} atacou!"

class Guerreiro(Personagem):
    pass

class Mago(Personagem):
    def lancar_magia(self):
        return f"{self.nome} lançou uma magia!"

g = Guerreiro("Thor", 100)
m = Mago("Merlim", 80)

print(g.nome)
print(g.atacar())

print(m.nome)
print(m.atacar())
print(m.lancar_magia())
