# Polimorfismo
# -Objetos diferentes que podem responder de maneiras diferentes ao mesmo método.

# Exemplo:

class Animal:
    def __init__(self, nome):
        self.nome = nome

    def fazer_som(self):
        raise NotImplemented
    
class Cachorro(Animal):
    def fazer_som(self):
        return f"{self.nome}: Auau!"

class Gato(Animal):
    def fazer_som(self):
        return f"{self.nome}: Miau!"
    

animais = [
    Cachorro("Fernando"),
    Gato("Gislene"),
    Cachorro("Bolt")
]

for animal in animais:
    print(animal.fazer_som())