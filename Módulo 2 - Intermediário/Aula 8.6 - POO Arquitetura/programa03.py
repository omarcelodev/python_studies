# Composição 

# -> Em vez de "é um" pense em: "tem um"

# -Errado(herança forçada):
class Animal:
    pass

class Ave(Animal):
    def voar(self):
        pass

# -Certo(Composição):

class PodeVoar:
    def voar(self):
        print("Voando...")

class Ave:
    def __init__(self):
        self.voo = PodeVoar()
    
# -Agora
# -> Pato voa, Galinha não, Drone também pode voar

# Composição = comportamento plugável
