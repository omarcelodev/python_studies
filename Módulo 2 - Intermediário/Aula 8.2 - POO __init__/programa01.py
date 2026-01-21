# __init__ é um método que roda automaticamente quando você cria um objeto.

"""
# Antes

cachorro = Cachorro()

cachorro.nome = "Maggie"
cachorro.idade = 2

# Funciona mas, objeto nasce incompleto, fácil esquecer atributo, código espalhado
"""

# Agora

class Cachorro:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def latir(self):
        return "Au au"
    
cachorro_1 = Cachorro("Maggie", 2)
cachorro_2 = Cachorro("Magali", 4)

# Nasce completo, sem gambiarra, sem risco