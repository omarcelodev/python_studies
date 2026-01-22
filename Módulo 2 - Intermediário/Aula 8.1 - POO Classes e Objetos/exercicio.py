class Cachorro:
    def latir(self):
        return "Au au"

cachorro_1 = Cachorro()
cachorro_2 = Cachorro()

cachorro_1.nome = "Maggie"
cachorro_2.nome = "Magali"

cachorro_1.idade = 2
cachorro_2.idade = 4 

print(f"{cachorro_1.nome}: {cachorro_1.latir()}")
print(f"{cachorro_2.nome}: {cachorro_2.latir()}")
