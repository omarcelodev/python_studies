class Animal:
    def __init__(self, nome):
        self.nome = nome

    def fazer_som(self):
        return f"{self.nome}: "

class Cachorro(Animal):
    def fazer_som(self):
        base = super().fazer_som()
        return base + "Auau!"

class Gato(Animal):
    def fazer_som(self):
        base = super().fazer_som()
        return base + "Miau!"

cachorro = Cachorro("Fernando")
gato = Gato("Gislene")

print(cachorro.fazer_som())
print(gato.fazer_som())