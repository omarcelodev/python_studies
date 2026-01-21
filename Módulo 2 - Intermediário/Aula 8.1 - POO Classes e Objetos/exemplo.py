class Cachorro:
    def __init__(self, nome, comida, sono):
        self.nome = nome
        self.comida = comida
        self.sono = sono

    def comer(self):
        self.comida -= 1

    def dormir(self):
        self.sono = False


cachorro_1 = Cachorro("Maggie", 5, False)
cachorro_2 = Cachorro("Jeremias", 3, True)

cachorro_1.comer()
cachorro_2.dormir()