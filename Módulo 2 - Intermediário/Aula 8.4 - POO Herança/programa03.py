# Sobrescrevendo métodos (customizar)

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
    
class Ladino(Personagem):
    def atacar(self): # Mesmo metodo com compartamentos diferentes
        return f"{self.nome} atacou furtivamente!"
    
g = Guerreiro("Thor", 100)
m = Mago("Merlim", 80)
l = Ladino("Jon", 90)

print(g.nome)
print(g.atacar())

print(m.nome)
print(m.atacar())
print(m.lancar_magia())

print(l.nome)
print(l.atacar())